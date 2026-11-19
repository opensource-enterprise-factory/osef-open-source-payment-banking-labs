#!/usr/bin/env python3
"""D06-2: explicitly gated synthetic-only PSP-A submission and PSP-B receipt check.

No Tazama API write. A strictly validated local report fixture and the D06-1
preview are prerequisites; live Tazama report schema must be verified separately.
NEVER point this lab client at any real PSP or payment endpoint.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

PSP_A_URL = "http://127.0.0.1:8091/submit"
PSP_B_URL = "http://127.0.0.1:8092/inbox"
TIMEOUT = 5
MAX_BODY = 32768
PREVIEW_PATH = Path(__file__).with_name("tazama-signal-preview.py")
POLICY_REF = "OSEF-D06-LAB-20261119"


def _load_preview():
    spec = importlib.util.spec_from_file_location("osef_d06_preview_for_submit", PREVIEW_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("preview unavailable")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.prepare_signal


def _opener():
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return None
    return urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())


def _open_status(url: str, *, payload: dict[str, Any] | None, key: str,
                 open_url=None) -> tuple[int, Any]:
    if url not in (PSP_A_URL, PSP_B_URL):
        return 0, None
    if not isinstance(key, str) or len(key) < 16 or any(c in key for c in "\r\n"):
        return 0, None
    method = "POST" if payload is not None else "GET"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"X-Lab-Key": key, "Content-Type": "application/json"})
    opener = open_url or _opener().open
    try:
        with opener(req, timeout=TIMEOUT) as res:
            if res.geturl() != url:
                return 0, None
            raw = res.read(MAX_BODY + 1)
            if len(raw) > MAX_BODY:
                return 0, None
            try:
                parsed = json.loads(raw)
            except (UnicodeError, ValueError):
                parsed = None
            return res.status, parsed
    except urllib.error.HTTPError as e:
        status = e.code
        e.close()
        return status, None
    except (urllib.error.URLError, ConnectionError, TimeoutError, OSError):
        return 0, None


def execute(report: Any, message_id: str, policy: Any, token_key: str,
            lab_key: str, *, enabled: bool = False,
            post=None, get=None) -> dict[str, str]:
    """No HTTP until ALL report, policy and key checks pass and enabled=True."""
    if not isinstance(policy, dict) or policy.get("approval_reference") != POLICY_REF:
        return {"decision": "NO_SEND", "reason": "POLICY_NOT_REVIEWED"}
    # Exact demo-only policy, approved by lab operator on 19 November 2026.
    if (policy.get("category"), policy.get("severity"), policy.get("recipient"),
        policy.get("expires_in_hours")) != ("suspicious-transfer", "medium", "psp-b", 1):
        return {"decision": "NO_SEND", "reason": "POLICY_MISMATCH"}
    prepared = _load_preview()(report, message_id, policy, token_key)
    if prepared.get("decision") != "PREVIEW_ONLY":
        return {"decision": "NO_SEND", "reason": prepared.get("reason", "INVALID_REPORT")}
    if not enabled:
        return {"decision": "PREVIEW_ONLY", "reason": "SEND_NOT_ENABLED"}
    if not isinstance(lab_key, str) or len(lab_key) < 16:
        return {"decision": "NO_SEND", "reason": "MISSING_PSP_LAB_KEY"}
    payload = prepared["signal"]
    post = post or (lambda p, k: _open_status(PSP_A_URL, payload=p, key=k))
    status, _ = post(payload, lab_key)
    if status == 409:
        # Duplicate means the relay has *previously* accepted this exact token.
        # Do not infer receipt: verify separately with PSP-B.
        return {"decision": "DUPLICATE", "reason": "PSP_A_409"}
    if status == 401:
        return {"decision": "NO_SEND", "reason": "PSP_A_UNAUTHORIZED"}
    if status in (0, 503):
        return {"decision": "NO_SEND", "reason": "PSP_A_UNAVAILABLE"}
    if status != 201:
        return {"decision": "NO_SEND", "reason": "PSP_A_REJECTED"}
    # Optional receipt read: only the PSP-B /inbox endpoint, never /signals direct.
    if get is None:
        get = lambda k: _open_status(PSP_B_URL, payload=None, key=k)
    code, body = get(lab_key)
    if code != 200 or not isinstance(body, dict) or not isinstance(body.get("signals"), list):
        return {"decision": "SENT", "reason": "RECEIPT_UNCONFIRMED"}
    matches = [x for x in body["signals"] if isinstance(x, dict)
               and x.get("transaction_token") == payload["transaction_token"]
               and x.get("recipient") == "psp-b"
               and x.get("category") == payload["category"]
               and x.get("severity") == payload["severity"]]
    return ({"decision": "SENT_AND_RECEIVED", "reason": "PSP_B_CONFIRMED"}
            if len(matches) == 1 else {"decision": "SENT", "reason": "RECEIPT_UNCONFIRMED"})


def main() -> int:
    parser = argparse.ArgumentParser(description="OSEF D06-2 synthetic lab controlled submit")
    parser.add_argument("--report", type=Path, required=True, help="Reviewed synthetic, sanitized report file")
    parser.add_argument("--policy", type=Path, required=True, help="Approved lab policy file")
    parser.add_argument("--msgid", required=True)
    parser.add_argument("--send-synthetic-lab", action="store_true",
                        help="Explicitly send one approved synthetic signal to PSP-A only")
    args = parser.parse_args()
    try:
        with args.report.open(encoding="utf-8") as f:
            report = json.load(f)
        with args.policy.open(encoding="utf-8") as f:
            policy = json.load(f)
        result = execute(report, args.msgid, policy,
                         os.environ.get("OSEF_FRAUD002_LAB_TOKEN_KEY", ""),
                         os.environ.get("LAB_USER_KEY", ""),
                         enabled=args.send_synthetic_lab)
    except (OSError, ValueError, UnicodeError, TypeError):
        result = {"decision": "NO_SEND", "reason": "INVALID_LOCAL_INPUT"}
    # No token, ID, report, raw API response, secret or HTTP body on stdout.
    print(json.dumps(result, sort_keys=True))
    return 0 if result["decision"] in ("PREVIEW_ONLY", "SENT_AND_RECEIVED", "DUPLICATE") else 2


if __name__ == "__main__":
    raise SystemExit(main())
