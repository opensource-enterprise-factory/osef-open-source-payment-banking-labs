#!/usr/bin/env python3
"""FRAUD-002 Gate D: inspect a saved Tazama report OFFLINE.

Strict dry-run: no HTTP client, no credentials, no PSP relay writes, no production use.
Validated lab statuses: NALT (no alert) and ALRT (alert candidate only).
Never send a signal and never infer FRAUD-001 severity from the Tazama score.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


# Gate D05 is limited to the exact observed synthetic public DockerHub profile.
# It authorizes a *candidate for human review*, NEVER a transmission.
EXPECTED_TYPOLOGY = "999-901-902@4.0.0"
EXPECTED_RULES = {"901@4.0.0", "902@4.0.0", "EFRuP@4.0.0"}
EXPECTED_WEIGHTS = {"901@4.0.0": {".01": 100, ".02": 200, ".03": 400},
                    "902@4.0.0": {".01": 100, ".02": 200, ".03": 400},
                    "EFRuP@4.0.0": {"none": 0}}


def _approved_alert_candidate(report: dict[str, Any]) -> bool:
    """Validate the observed profile; reject ambiguous/malformed data."""
    tadp = report.get("tadpResult")
    if not isinstance(tadp, dict):
        return False
    typologies = tadp.get("typologyResult")
    if not isinstance(typologies, list) or len(typologies) != 1:
        return False
    t = typologies[0]
    if not isinstance(t, dict) or t.get("cfg") != EXPECTED_TYPOLOGY:
        return False
    workflow = t.get("workflow")
    if not isinstance(workflow, dict):
        return False
    if workflow.get("alertThreshold") != 300 or workflow.get("interdictionThreshold") != 500:
        return False
    if workflow.get("flowProcessor") != "EFRuP@4.0.0":
        return False
    # Reject bools: Python treats True as an int.
    score = t.get("result")
    if type(score) not in (int, float) or not 300 <= score:
        return False
    rule_results = t.get("ruleResults")
    if not isinstance(rule_results, list) or len(rule_results) != 3:
        return False
    seen = set()
    total = 0
    for rule in rule_results:
        if not isinstance(rule, dict):
            return False
        rule_id = rule.get("id")
        band = rule.get("subRuleRef")
        weight = rule.get("wght")
        if rule_id not in EXPECTED_RULES or rule_id in seen:
            return False
        if type(weight) not in (int, float) or EXPECTED_WEIGHTS[rule_id].get(band) != weight:
            return False
        seen.add(rule_id)
        total += weight
    return seen == EXPECTED_RULES and total == score


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
    if status == "ALRT":
        if _approved_alert_candidate(report):
            # An analyst must still approve category, severity and recipient.
            # No signal schema is constructed, persisted, or sent.
            return {"decision": "REVIEW_ONLY", "reason": "ALRT_CANDIDATE"}
        return {"decision": "NO_PUBLISH", "reason": "ALRT_NOT_QUALIFIED"}
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
    return 0 if result["reason"] in ("NALT", "REPORT_NOT_READY", "ALRT_CANDIDATE") else 2


if __name__ == "__main__":
    raise SystemExit(main())
