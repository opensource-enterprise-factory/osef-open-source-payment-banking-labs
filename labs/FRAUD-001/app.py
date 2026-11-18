"""FRAUD-001: échange antifraude pédagogique. Données synthétiques uniquement.

Ce prototype n'est ni un switch de paiement ni une implémentation OFTA officielle.
Ne jamais connecter cette application à un système de production.
"""
import hmac
import os
import sqlite3
import uuid
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Literal

import httpx
from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

ROLE = os.environ.get("ROLE", "")
RELAY_URL = os.environ.get("RELAY_URL", "http://relay:8000")
DB_PATH = os.environ.get("DATABASE_PATH", "/data/relay.db")
app = FastAPI(title=f"OSEF FRAUD-001 ({ROLE})", version="0.1.0")


class Signal(BaseModel):
    # Le préfixe demo- rend explicite l'interdiction de transactions réelles.
    transaction_token: str = Field(pattern=r"^demo-[A-Za-z0-9-]{8,64}$", max_length=69)
    category: Literal["suspicious-transfer", "account-takeover", "social-engineering"]
    severity: Literal["low", "medium", "high"]
    recipient: Literal["psp-b"]
    expires_in_hours: int = Field(ge=1, le=24)


def now() -> datetime:
    return datetime.now(timezone.utc)


def require_key(provided: str | None, expected: str) -> None:
    # compare_digest limite les comparaisons temporelles ; ceci reste une clé LAB.
    if not provided or not expected or not hmac.compare_digest(provided, expected):
        raise HTTPException(status_code=401, detail="Unauthorized")


def require_relay_role(provided: str | None, allowed: tuple[str, ...]) -> str:
    for name in allowed:
        expected = os.environ.get("PSP_A_KEY" if name == "psp-a" else "PSP_B_KEY", "")
        if expected and provided and hmac.compare_digest(provided, expected):
            return name
    raise HTTPException(status_code=401, detail="Unauthorized")


@contextmanager
def connect():
    with sqlite3.connect(DB_PATH, timeout=10) as db:
        db.row_factory = sqlite3.Row
        yield db
        db.commit()


def initialize() -> None:
    if ROLE != "relay":
        return
    with connect() as db:
        db.execute("""CREATE TABLE IF NOT EXISTS signals (
            id TEXT PRIMARY KEY,
            token TEXT UNIQUE NOT NULL,
            origin TEXT NOT NULL,
            recipient TEXT NOT NULL,
            category TEXT NOT NULL,
            severity TEXT NOT NULL,
            created_at TEXT NOT NULL,
            expires_at TEXT NOT NULL
        )""")
        db.execute("""CREATE TABLE IF NOT EXISTS audit (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            actor TEXT NOT NULL,
            action TEXT NOT NULL,
            outcome TEXT NOT NULL
        )""")


initialize()


def audit(db: sqlite3.Connection, actor: str, action: str, outcome: str) -> None:
    # Ne pas enregistrer les clés ni les charges utiles dans le journal.
    db.execute(
        "INSERT INTO audit(timestamp,actor,action,outcome) VALUES (?,?,?,?)",
        (now().isoformat(), actor, action, outcome),
    )


@app.get("/health")
def health():
    return {"status": "ok", "role": ROLE}


@app.post("/signals", status_code=201)
def create_signal(payload: Signal, x_api_key: str | None = Header(default=None)):
    if ROLE != "relay":
        raise HTTPException(status_code=404)
    actor = require_relay_role(x_api_key, ("psp-a",))
    timestamp = now()
    uid = str(uuid.uuid4())
    try:
        with connect() as db:
            db.execute(
                """INSERT INTO signals(id,token,origin,recipient,category,severity,created_at,expires_at)
                   VALUES (?,?,?,?,?,?,?,?)""",
                (uid, payload.transaction_token, actor, payload.recipient,
                 payload.category, payload.severity, timestamp.isoformat(),
                 (timestamp + timedelta(hours=payload.expires_in_hours)).isoformat()),
            )
            audit(db, actor, "create", "accepted")
    except sqlite3.IntegrityError:
        with connect() as db:
            audit(db, actor, "create", "duplicate-rejected")
        raise HTTPException(status_code=409, detail="Duplicate synthetic token")
    return {"id": uid, "status": "accepted", "created_at": timestamp.isoformat()}


@app.get("/signals")
def read_signals(x_api_key: str | None = Header(default=None)):
    if ROLE != "relay":
        raise HTTPException(status_code=404)
    actor = require_relay_role(x_api_key, ("psp-b",))
    with connect() as db:
        rows = db.execute(
            """SELECT token,origin,recipient,category,severity,created_at,expires_at
               FROM signals WHERE recipient=? AND expires_at>?
               ORDER BY created_at DESC LIMIT 100""",
            (actor, now().isoformat()),
        ).fetchall()
        audit(db, actor, "read", "authorized")
    return {"signals": [
        {"transaction_token": r["token"], "origin": r["origin"],
         "recipient": r["recipient"], "category": r["category"],
         "severity": r["severity"], "created_at": r["created_at"],
         "expires_at": r["expires_at"]} for r in rows
    ]}


@app.get("/audit")
def read_audit(x_api_key: str | None = Header(default=None)):
    if ROLE != "relay":
        raise HTTPException(status_code=404)
    require_key(x_api_key, os.environ.get("ADMIN_KEY", ""))
    with connect() as db:
        rows = db.execute(
            "SELECT timestamp,actor,action,outcome FROM audit ORDER BY id DESC LIMIT 100"
        ).fetchall()
    return {"events": [dict(r) for r in rows]}


@app.post("/submit", status_code=201)
async def submit(payload: Signal, x_lab_key: str | None = Header(default=None)):
    if ROLE != "psp-a":
        raise HTTPException(status_code=404)
    require_key(x_lab_key, os.environ.get("LAB_USER_KEY", ""))
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.post(
                f"{RELAY_URL}/signals",
                headers={"X-API-Key": os.environ["PSP_A_KEY"]},
                json=payload.model_dump(),
            )
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="Lab relay unavailable")
    if response.status_code not in (201, 409):
        raise HTTPException(status_code=502, detail="Relay rejected request")
    if response.status_code == 409:
        raise HTTPException(status_code=409, detail="Synthetic token already exists")
    return response.json()


@app.get("/inbox")
async def inbox(x_lab_key: str | None = Header(default=None)):
    if ROLE != "psp-b":
        raise HTTPException(status_code=404)
    require_key(x_lab_key, os.environ.get("LAB_USER_KEY", ""))
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(
                f"{RELAY_URL}/signals",
                headers={"X-API-Key": os.environ["PSP_B_KEY"]},
            )
        response.raise_for_status()
    except httpx.HTTPError:
        raise HTTPException(status_code=503, detail="Lab relay unavailable")
    return response.json()


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def demo():
    if ROLE not in ("relay", "psp-a", "psp-b"):
        raise HTTPException(status_code=404)
    page = Path(__file__).with_name("demo.html").read_text(encoding="utf-8")
    return HTMLResponse(page.replace("__FRAUD_ROLE__", ROLE), headers={"Cache-Control": "no-store"})
