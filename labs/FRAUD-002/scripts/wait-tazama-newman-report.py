#!/usr/bin/env python3
"""Wait for one synthetic Tazama Admin report without revealing its contents.

Reads a Newman-exported globals JSON. Only GET to the fixed 127.0.0.1:5100
Admin URL; no transaction submission, no external service, no report files.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ID = re.compile(r"^[0-9a-fA-F]{32}$")
DEFAULT_ATTEMPTS = 30
DEFAULT_INTERVAL = 2.0


def message_id_from_globals(payload: object) -> str:
    if not isinstance(payload, dict) or not isinstance(payload.get("values"), list):
        raise ValueError("Invalid Newman globals format")
    ids = [v.get("value") for v in payload["values"]
           if isinstance(v, dict) and v.get("key") == "messageIdPacs002"
           and v.get("enabled", True) is not False]
    if len(ids) != 1 or not isinstance(ids[0], str) or not ID.fullmatch(ids[0]):
        raise ValueError("Missing or invalid pacs.002 message identifier")
    return ids[0]


def wait_until_report(msgid: str, *, fetch, sleep=time.sleep, attempts=DEFAULT_ATTEMPTS,
                      interval=DEFAULT_INTERVAL) -> str:
    """Return READY on a matching fully materialized Admin report, else raise."""
    if not ID.fullmatch(msgid) or not 1 <= attempts <= 60 or not 0 <= interval <= 10:
        raise ValueError("Invalid polling parameters")
    for index in range(attempts):
        status, payload = fetch(msgid)
        if status == 200:
            if not isinstance(payload, dict):
                raise RuntimeError("INVALID_REPORT")
            body = payload.get("data")
            if not isinstance(body, dict):
                raise RuntimeError("INVALID_REPORT")
            transaction = body.get("transaction")
            header = (
                transaction.get("FIToFIPmtSts", {}).get("GrpHdr", {})
                if isinstance(transaction, dict) else {}
            )
            if not (isinstance(body.get("report"), dict) and body["report"]
                    and body.get("transactionID") == msgid
                    and isinstance(header, dict) and header.get("MsgId") == msgid):
                raise RuntimeError("REPORT_IDENTITY_OR_CONTENT_MISMATCH")
            return "READY"
        if status != 204:
            raise RuntimeError("ADMIN_HTTP_ERROR")
        if index + 1 < attempts:
            sleep(interval)
    raise RuntimeError("REPORT_NOT_READY_AFTER_BOUNDED_POLL")


def main() -> int:
    parser = argparse.ArgumentParser(description="Bounded Tazama report readiness probe")
    parser.add_argument("--globals", type=Path, required=True)
    parser.add_argument("--attempts", type=int, default=DEFAULT_ATTEMPTS)
    parser.add_argument("--interval", type=float, default=DEFAULT_INTERVAL)
    args = parser.parse_args()

    # Use the existing read-only client: hardcoded loopback, bounded body,
    # disabled proxies and redirects, fail-closed handling of network errors.
    spec = importlib.util.spec_from_file_location(
        "osef_tazama_readonly", SCRIPT_DIR / "tazama-read-only-dry-run.py")
    if spec is None or spec.loader is None:
        print("[BLOCK] READ_ONLY_CLIENT_UNAVAILABLE")
        return 2
    reader = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reader)
    try:
        if args.globals.stat().st_size > 1_048_576:
            raise ValueError("GLOBALS_TOO_LARGE")
        with args.globals.open(encoding="utf-8") as file:
            msgid = message_id_from_globals(json.load(file))
        status = wait_until_report(msgid, fetch=reader._fetch_once,
                                   attempts=args.attempts, interval=args.interval)
        print("[OK] Tazama Admin report READY; identity verified")
        return 0
    except (ValueError, OSError, UnicodeError, RuntimeError) as exc:
        # Do not print JSON payload, IDs, tokens or external exception detail.
        reason = str(exc) if isinstance(exc, RuntimeError) and str(exc) in (
            "INVALID_REPORT", "REPORT_IDENTITY_OR_CONTENT_MISMATCH",
            "ADMIN_HTTP_ERROR", "REPORT_NOT_READY_AFTER_BOUNDED_POLL") else "INVALID_INPUT_OR_IO"
        print("[BLOCK] " + reason)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
