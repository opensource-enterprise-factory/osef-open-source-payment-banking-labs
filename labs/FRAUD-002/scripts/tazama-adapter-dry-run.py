#!/usr/bin/env python3
"""FRAUD-002 Gate D: inspect a saved Tazama report OFFLINE.

Strict dry-run: no HTTP client, no credentials, no PSP relay writes, no production use.
The only validated report status in this lab is NALT (no alert).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def assess_report(payload: Any, *, http_status: int = 200) -> dict[str, str]:
    """Return only a non-sensitive decision summary. Never return report fields."""
    if http_status == 204:
        return {"decision": "NO_PUBLISH", "reason": "REPORT_NOT_READY"}
    if http_status != 200:
        return {"decision": "NO_PUBLISH", "reason": "SOURCE_HTTP_ERROR"}
    if not isinstance(payload, dict):
        return {"decision": "NO_PUBLISH", "reason": "INVALID_REPORT"}
    data = payload.get("data")
    if not isinstance(data, dict):
        return {"decision": "NO_PUBLISH", "reason": "INVALID_REPORT"}
    report = data.get("report")
    if not isinstance(report, dict):
        return {"decision": "NO_PUBLISH", "reason": "INVALID_REPORT"}
    if payload.get("message") != "Report was found":
        return {"decision": "NO_PUBLISH", "reason": "UNCONFIRMED_REPORT"}

    status = report.get("status")
    if status == "NALT":
        # A confirmed NALT is not an alert even if numeric rule weights are non-zero.
        return {"decision": "NO_PUBLISH", "reason": "NALT"}
    # No positive fraud status is approved. Even a score >= threshold cannot
    # authorize forwarding without an explicit, versioned business rule.
    return {"decision": "NO_PUBLISH", "reason": "UNAPPROVED_STATUS"}


def main() -> int:
    parser = argparse.ArgumentParser(description="FRAUD-002 offline Tazama dry-run classifier")
    parser.add_argument("--report", type=Path, help="Local, sanitized JSON fixture only")
    parser.add_argument("--http-status", type=int, default=200, help="Observed HTTP status (default: 200)")
    args = parser.parse_args()

    if args.http_status == 204:
        result = assess_report(None, http_status=204)
    elif not args.report:
        parser.error("--report is required unless --http-status 204")
    else:
        try:
            # Local file only: never fetch from HTTP or expose full transaction details.
            with args.report.open("r", encoding="utf-8") as handle:
                payload = json.load(handle)
            result = assess_report(payload, http_status=args.http_status)
        except (OSError, ValueError, UnicodeError):
            result = {"decision": "NO_PUBLISH", "reason": "UNREADABLE_REPORT"}
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result["reason"] in ("NALT", "REPORT_NOT_READY") else 2


if __name__ == "__main__":
    raise SystemExit(main())
