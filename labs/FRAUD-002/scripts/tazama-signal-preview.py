#!/usr/bin/env python3
"""FRAUD-002 D06-1: preview a minimal FRAUD-001 signal, NEVER transmit it.

Accepts ONLY synthetic reports, an explicit lab-only approval policy and a
separate local HMAC key. No HTTP client, POST, database or on-disk state.
This is a design/test step, NOT a production fraud decision.
"""
from __future__ import annotations

import argparse
import hashlib
import hmac
import importlib.util
import json
import os
import re
from pathlib import Path
from typing import Any

MSGID = re.compile(r"^[0-9a-fA-F]{32}$")
SAFE_APPROVAL = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{5,63}$")
CLASSIFIER = Path(__file__).with_name("tazama-adapter-dry-run.py")


def _classifier():
    spec = importlib.util.spec_from_file_location("osef_d06_classifier", CLASSIFIER)
    if spec is None or spec.loader is None:
        raise RuntimeError("classifier unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.assess_report


def _deny(reason: str) -> dict[str, Any]:
    return {"decision": "NO_PUBLISH", "reason": reason}


def prepare_signal(report_payload: Any, message_id: str, policy: Any,
                   secret: str | bytes) -> dict[str, Any]:
    """Prepare a signal only in memory, for a reviewed synthetic lab policy.

    The returned payload is internal test data; CLI deliberately prints no
    token or other signal fields. Nothing is sent or persisted.
    """
    if not isinstance(message_id, str) or not MSGID.fullmatch(message_id):
        return _deny("INVALID_MESSAGE_ID")
    if _classifier()(report_payload) != {
        "decision": "REVIEW_ONLY", "reason": "ALRT_CANDIDATE"
    }:
        return _deny("REPORT_NOT_QUALIFIED")
    data = report_payload.get("data", {})
    # An unrelated report must not be mapped to an operator-supplied ID.
    if data.get("transactionID") != message_id:
        return _deny("MESSAGE_ID_MISMATCH")
    transaction = data.get("transaction")
    if not isinstance(transaction, dict):
        return _deny("INVALID_TRANSACTION_BINDING")
    fi = transaction.get("FIToFIPmtSts")
    header = fi.get("GrpHdr") if isinstance(fi, dict) else None
    if not isinstance(header, dict) or header.get("MsgId") != message_id:
        return _deny("MESSAGE_ID_MISMATCH")
    if not isinstance(policy, dict):
        return _deny("UNAPPROVED_POLICY")
    # Approval must refer to an explicit lab review outside the CLI; a
    # policy file alone is NOT evidence of institutional approval.
    if policy.get("approved_for_lab") is not True:
        return _deny("UNAPPROVED_POLICY")
    ref = policy.get("approval_reference")
    if not isinstance(ref, str) or not SAFE_APPROVAL.fullmatch(ref):
        return _deny("UNAPPROVED_POLICY")
    category = policy.get("category")
    severity = policy.get("severity")
    recipient = policy.get("recipient")
    ttl = policy.get("expires_in_hours")
    if category not in ("suspicious-transfer", "account-takeover", "social-engineering"):
        return _deny("INVALID_POLICY")
    if severity not in ("low", "medium", "high") or recipient != "psp-b":
        return _deny("INVALID_POLICY")
    if type(ttl) is not int or not 1 <= ttl <= 24:
        return _deny("INVALID_POLICY")
    key = secret.encode("utf-8") if isinstance(secret, str) else secret
    if not isinstance(key, bytes) or len(key) < 32:
        return _deny("MISSING_LAB_KEY")
    # HMAC prevents plain hashing from exposing the transaction ID.
    # Only synthetic message IDs are allowed. Stable on retry, different
    # with a separate secret; the secret must never enter Git or logs.
    digest = hmac.new(key, b"OSEF-FRAUD-002-D06|" + message_id.lower().encode(),
                      hashlib.sha256).hexdigest()[:32]
    minimal = {
        "transaction_token": "demo-" + digest,
        "category": category,
        "severity": severity,
        "recipient": "psp-b",
        "expires_in_hours": ttl,
    }
    return {"decision": "PREVIEW_ONLY", "reason": "APPROVED_LAB_CANDIDATE",
            "signal": minimal}


def main() -> int:
    parser = argparse.ArgumentParser(description="FRAUD-002 offline signal preview, never POST")
    parser.add_argument("--report", type=Path, required=True,
                        help="Sanitized synthetic JSON fixture outside the repository")
    parser.add_argument("--msgid", required=True, help="Synthetic pacs.002 message ID")
    parser.add_argument("--policy", type=Path, required=True,
                        help="Locally approved lab policy JSON, not a production authorization")
    args = parser.parse_args()
    try:
        # Both inputs are LOCAL files. Never print their contents.
        with args.report.open(encoding="utf-8") as f:
            report = json.load(f)
        with args.policy.open(encoding="utf-8") as f:
            policy = json.load(f)
        result = prepare_signal(report, args.msgid, policy,
                                os.environ.get("OSEF_FRAUD002_LAB_TOKEN_KEY", ""))
    except (OSError, ValueError, UnicodeError, TypeError):
        result = _deny("INVALID_LOCAL_INPUT")
    # Never display the token, policy reference, report or personal data.
    print(json.dumps({"decision": result["decision"], "reason": result["reason"]},
                     sort_keys=True))
    return 0 if result["decision"] == "PREVIEW_ONLY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
