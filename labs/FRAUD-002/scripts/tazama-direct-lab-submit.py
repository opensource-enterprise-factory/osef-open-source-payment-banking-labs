#!/usr/bin/env python3
"""FRAUD-002 Gate E05: in-memory real Tazama Admin GET to approved D06 lab flow.

No raw report file, no credentials to Tazama (public lab profile). Hard-coded
loopback URLs only. Never POST unless --send-synthetic-lab is explicitly set.
No report, token or account details on stdout. Not for real customers.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
MAX_POLICY_BYTES = 16384


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module unavailable")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _deny(reason: str) -> dict[str, str]:
    return {"decision": "NO_SEND", "reason": reason}


def process_message(message_id: str, policy: Any, token_key: str, lab_key: str,
                    *, enabled: bool = False, fetch=None, submit=None) -> dict[str, str]:
    """Read one genuine lab report and use the D06-2 strict, reviewed gate.

    Inject fetch/submit in unit tests. No network is touched for malformed IDs
    or unapproved policies. HTTP GET data stays in RAM and is never printed.
    """
    read = _load(HERE / "tazama-read-only-dry-run.py", "osef_e05_tazama_reader")
    send = _load(HERE / "tazama-controlled-submit.py", "osef_e05_submit")
    if not isinstance(message_id, str) or not read.ID_PATTERN.fullmatch(message_id):
        return _deny("INVALID_MESSAGE_ID")
    if not isinstance(policy, dict) or (
        policy.get("approved_for_lab") is not True
        or policy.get("approval_reference") != send.POLICY_REF
        or (policy.get("category"), policy.get("severity"), policy.get("recipient"),
            policy.get("expires_in_hours")) !=
            ("suspicious-transfer", "medium", "psp-b", 1)
    ):
        return _deny("POLICY_NOT_REVIEWED")
    if not isinstance(token_key, str) or len(token_key.encode("utf-8")) < 32:
        return _deny("MISSING_LAB_TOKEN_KEY")
    if enabled and (not isinstance(lab_key, str) or len(lab_key) < 16):
        return _deny("MISSING_PSP_LAB_KEY")
    fetch = fetch or read._fetch_once
    try:
        status, payload = fetch(message_id)
    except Exception:
        return _deny("TAZAMA_UNAVAILABLE")
    if status != 200:
        return _deny("TAZAMA_NOT_READY" if status == 204 else "TAZAMA_UNAVAILABLE")
    if not isinstance(payload, dict):
        return _deny("INVALID_TAZAMA_REPORT")

    # execute() revalidates both transaction identifiers, typology, weights,
    # explicitly approved policy and the lab-only destination before POST.
    kwargs = {"enabled": enabled}
    if submit is not None:
        kwargs["post"], kwargs["get"] = submit
    return send.execute(payload, message_id, policy, token_key, lab_key, **kwargs)


def main() -> int:
    p = argparse.ArgumentParser(description="Read real Tazama lab ALRT; no POST by default")
    p.add_argument("--msgid", required=True, help="synthetic pacs.002 message ID, 32 hex chars")
    p.add_argument("--policy", type=Path, required=True, help="reviewed D06 lab policy JSON")
    p.add_argument("--send-synthetic-lab", action="store_true",
                   help="one real synthetic lab submission PSP A -> relay -> PSP B")
    args = p.parse_args()
    try:
        if args.policy.stat().st_size > MAX_POLICY_BYTES:
            result = _deny("POLICY_TOO_LARGE")
        else:
            with args.policy.open(encoding="utf-8") as f:
                policy = json.load(f)
            result = process_message(
                args.msgid, policy,
                os.environ.get("OSEF_FRAUD002_LAB_TOKEN_KEY", ""),
                os.environ.get("LAB_USER_KEY", ""),
                enabled=args.send_synthetic_lab,
            )
    except (OSError, UnicodeError, ValueError):
        result = _deny("INVALID_POLICY_FILE")
    print(json.dumps(result, sort_keys=True))
    return 0 if result["decision"] in ("PREVIEW_ONLY", "SENT_AND_RECEIVED", "DUPLICATE") else 2


if __name__ == "__main__":
    raise SystemExit(main())
