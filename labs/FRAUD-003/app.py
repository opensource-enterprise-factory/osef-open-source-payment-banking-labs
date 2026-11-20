"""FRAUD-003 Gate 2: three fictitious institutions, isolated signal inboxes.

Synthetic data only. This is NOT a Tazama/OFTA integration or a production payment API.
"""
import hmac
import os
import sqlite3
from contextlib import asynccontextmanager, contextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Literal
from uuid import uuid4

from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

INSTITUTIONS = ("demo-bank-a", "demo-psp-b", "demo-mobile-c")
KEY_ENV = {
    "demo-bank-a": "FRAUD003_BANK_A_KEY",
    "demo-psp-b": "FRAUD003_PSP_B_KEY",
    "demo-mobile-c": "FRAUD003_MOBILE_C_KEY",
}


class SignalIn(BaseModel):
    # Forbid any unexpected fields, including customer/account/payment information.
    model_config = {"extra": "forbid"}
    signal_id: str = Field(pattern=r"^demo-[A-Za-z0-9-]{8,64}$", max_length=69)
    category: Literal["suspicious-transfer", "account-takeover", "social-engineering"]
    severity: Literal["low", "medium", "high"]
    scenario_ref: str = Field(pattern=r"^demo-[A-Za-z0-9-]{8,64}$", max_length=69)
    expires_in_hours: int = Field(ge=1, le=24)


def create_app(db_path: str | None = None, keys: dict[str, str] | None = None) -> FastAPI:
    database = db_path if db_path is not None else os.getenv("FRAUD003_DB_PATH", "/data/fraud003.db")
    secrets = dict(keys) if keys is not None else {
        institution: os.getenv(envname, "") for institution, envname in KEY_ENV.items()
    }
    # Every key must be nonempty, distinct and nontrivial. No fallback shared LAB_USER_KEY.
    configured = (
        set(secrets) == set(INSTITUTIONS)
        and all(isinstance(v, str) and len(v) >= 32 for v in secrets.values())
        and len(set(secrets.values())) == len(INSTITUTIONS)
    )

    @contextmanager
    def connection():
        with sqlite3.connect(database, timeout=10) as db:
            db.row_factory = sqlite3.Row
            yield db
            db.commit()

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        if not configured:
            raise RuntimeError("Configure three distinct FRAUD003_*_KEY values (>=32 characters)")
        Path(database).parent.mkdir(parents=True, exist_ok=True)
        with connection() as db:
            db.execute("""CREATE TABLE IF NOT EXISTS signals(
                institution TEXT NOT NULL, signal_id TEXT NOT NULL,
                category TEXT NOT NULL, severity TEXT NOT NULL,
                scenario_ref TEXT NOT NULL, created_at TEXT NOT NULL,
                expires_at TEXT NOT NULL,
                PRIMARY KEY(institution, signal_id)
            )""")
            db.execute("""CREATE TABLE IF NOT EXISTS audit(
                id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT NOT NULL,
                institution TEXT NOT NULL, action TEXT NOT NULL, outcome TEXT NOT NULL
            )""")
        yield

    api = FastAPI(title="OSEF FRAUD-003 Gate 2 — synthetic only", lifespan=lifespan)

    def identify(provided: str | None) -> str:
        if not provided or not configured:
            raise HTTPException(status_code=401, detail="Unauthorized")
        # Evaluate all comparisons to avoid easy early-return timing distinctions.
        matches = [
            hmac.compare_digest(provided, secrets[institution]) for institution in INSTITUTIONS
        ]
        if sum(matches) != 1:
            raise HTTPException(status_code=401, detail="Unauthorized")
        return INSTITUTIONS[matches.index(True)]

    def log(db: sqlite3.Connection, institution: str, action: str, outcome: str):
        db.execute(
            "INSERT INTO audit(timestamp,institution,action,outcome) VALUES(?,?,?,?)",
            (datetime.now(timezone.utc).isoformat(), institution, action, outcome),
        )

    # Public, localhost-only teaching page. API operations still require the
    # selected institution's key; the page does not receive any secrets.
    @api.get("/", include_in_schema=False)
    def dashboard():
        return FileResponse(
            Path(__file__).with_name("dashboard.html"),
            media_type="text/html",
            headers={
                "Cache-Control": "no-store",
                "Content-Security-Policy": "default-src 'none'; script-src 'self'; style-src 'unsafe-inline'; connect-src 'self'; img-src 'none'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'",
                "X-Content-Type-Options": "nosniff",
                "Referrer-Policy": "no-referrer",
            },
        )

    @api.get("/ui.js", include_in_schema=False)
    def dashboard_js():
        return FileResponse(
            Path(__file__).with_name("dashboard.js"),
            media_type="application/javascript",
            headers={
                "Cache-Control": "no-store",
                "X-Content-Type-Options": "nosniff",
                "Referrer-Policy": "no-referrer",
            },
        )

    @api.get("/health")
    def health():
        return {"status": "ok", "service": "fraud-003-gate2"}

    @api.post("/signals", status_code=201)
    def create_signal(payload: SignalIn, x_lab_key: str | None = Header(default=None)):
        institution = identify(x_lab_key)
        timestamp = datetime.now(timezone.utc)
        with connection() as db:
            try:
                db.execute(
                    """INSERT INTO signals(institution,signal_id,category,severity,
                       scenario_ref,created_at,expires_at) VALUES(?,?,?,?,?,?,?)""",
                    (
                        institution, payload.signal_id, payload.category, payload.severity,
                        payload.scenario_ref, timestamp.isoformat(),
                        (timestamp + timedelta(hours=payload.expires_in_hours)).isoformat(),
                    ),
                )
            except sqlite3.IntegrityError:
                # Write the audit in a separate successful transaction;
                # raising inside the context would roll back the audit entry.
                db.rollback()
                log(db, institution, "create", "duplicate")
                duplicate = True
            else:
                log(db, institution, "create", "accepted")
                duplicate = False
        if duplicate:
            raise HTTPException(status_code=409, detail="Duplicate signal ID for institution")
        return {"signal_id": payload.signal_id, "status": "accepted"}

    @api.get("/signals")
    def list_signals(x_lab_key: str | None = Header(default=None)):
        institution = identify(x_lab_key)
        with connection() as db:
            rows = db.execute(
                """SELECT signal_id, category, severity, scenario_ref,
                          created_at, expires_at
                   FROM signals WHERE institution=? AND expires_at>?
                   ORDER BY created_at DESC LIMIT 100""",
                (institution, datetime.now(timezone.utc).isoformat()),
            ).fetchall()
            log(db, institution, "list", "authorized")
        return {"institution": institution, "signals": [dict(r) for r in rows]}

    @api.get("/signals/{signal_id}")
    def get_signal(signal_id: str, x_lab_key: str | None = Header(default=None)):
        institution = identify(x_lab_key)
        with connection() as db:
            row = db.execute(
                """SELECT signal_id, category, severity, scenario_ref,
                          created_at, expires_at FROM signals
                   WHERE institution=? AND signal_id=? AND expires_at>?""",
                (institution, signal_id, datetime.now(timezone.utc).isoformat()),
            ).fetchone()
            log(db, institution, "get", "authorized" if row else "not-found")
        if row is None:
            # Do not disclose whether a signal belongs to another institution.
            raise HTTPException(status_code=404, detail="Not found")
        return dict(row)

    return api


app = create_app()
