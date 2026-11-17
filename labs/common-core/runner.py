#!/usr/bin/env python3
"""OSEF Academy TC-01..TC-07 — offline synthetic teaching exercises.

No external packages, network operations, card data, or payment execution.
Python >= 3.10 (annotation support). All values are invented.
"""
import argparse
import hashlib
import json
from dataclasses import dataclass, field
from typing import Any


def tc01_manifest() -> dict[str, str]:
    """Exercise Git/reproducibility: hash stable fictional training data."""
    sample = b"OSEF-ACADEMY|LAB-ONLY|TX-FAKE-001|1000"
    return {"fixture": sample.decode(), "sha256": hashlib.sha256(sample).hexdigest()}


def tc02_api(method: str, path: str, data: dict, token: str) -> tuple[int, dict]:
    """In-process HTTP contract mock, not a listening API server."""
    if token != "LAB-ONLY":
        return 401, {"error": "unauthorized"}
    if method != "POST" or path != "/fake-payments":
        return 404, {"error": "not_found"}
    if not isinstance(data, dict) or data.get("amount_minor") not in range(1, 1000001):
        return 422, {"error": "invalid_amount"}
    if not isinstance(data.get("reference"), str) or not data["reference"].startswith("FAKE-"):
        return 422, {"error": "invalid_reference"}
    return 201, {"id": "TX-FAKE-001", "state": "RECEIVED"}


TRANSITIONS = {
    "RECEIVED": {"APPROVED", "DECLINED", "UNKNOWN"},
    "UNKNOWN": {"APPROVED", "DECLINED"},
    "APPROVED": set(),
    "DECLINED": set(),
}


def tc03_transition(current: str, target: str) -> str:
    """Finite state simulation; UNKNOWN is not a declined transaction."""
    if target not in TRANSITIONS.get(current, set()):
        raise ValueError(f"invalid transition: {current} -> {target}")
    return target


@dataclass
class SyntheticLedger:
    """Toy double-entry journal: values are integer minor units, not money."""
    balances: dict[str, int] = field(default_factory=lambda: {"FAKE-A": 10000, "FAKE-B": 0})
    seen: dict[str, tuple[str, str, int]] = field(default_factory=dict)
    journal: list[tuple[str, str, int]] = field(default_factory=list)

    def transfer(self, key: str, debit: str, credit: str, amount: int) -> bool:
        if not key.startswith("LAB-") or debit == credit:
            raise ValueError("invalid synthetic transaction")
        if type(amount) is not int or amount <= 0:
            raise ValueError("amount must be a positive integer")
        if debit not in self.balances or credit not in self.balances:
            raise ValueError("unknown toy account")
        operation = (debit, credit, amount)
        if key in self.seen:
            if self.seen[key] != operation:
                raise ValueError("idempotency key reused with different payload")
            return False
        if self.balances[debit] < amount:
            raise ValueError("insufficient synthetic balance")
        self.balances[debit] -= amount
        self.balances[credit] += amount
        self.journal.extend([(debit, -amount), (credit, amount)])
        self.seen[key] = operation
        return True

    def balanced(self) -> bool:
        return sum(v for _, v in self.journal) == 0


def tc05_authorize(scope: str, token: str) -> bool:
    """Simulated authorization; this string token must never be used in real systems."""
    return token == "LAB-ROLE:writer" and scope == "payment:write"


def tc05_redact(record: dict[str, Any]) -> dict[str, Any]:
    """Allowlist logging; discard other keys rather than try to mask secrets."""
    return {key: record[key] for key in ("event", "state", "correlation_id")
            if key in record}


def tc06_resolve(initial: str, response: str | None) -> tuple[str, str]:
    """No response means UNKNOWN and requires reconciliation, never auto-reversal."""
    if initial != "RECEIVED":
        raise ValueError("expected a newly received synthetic request")
    if response is None:
        return "UNKNOWN", "query_status_before_any_compensation"
    if response == "ACCEPT":
        return "APPROVED", "record_result"
    if response == "DECLINE":
        return "DECLINED", "record_result"
    raise ValueError("unsupported fictional response")


def tc07_review() -> dict[str, Any]:
    """Machine-readable BDAT/ADR skeleton; not proof of implementation."""
    return {
        "business": ["fictitious payer", "fictitious receiver"],
        "data": ["synthetic order", "toy journal"],
        "application": ["in-process contract mock", "toy ledger"],
        "technology": ["Python standard library", "offline test runner"],
        "decision": "avoid all external payment rails",
        "status": "conceptual_lab_only",
    }


def run(which: str) -> dict[str, Any]:
    """Demonstration, not a certification or live financial service."""
    if which == "TC-01":
        return tc01_manifest()
    if which == "TC-02":
        status, body = tc02_api("POST", "/fake-payments",
                                {"amount_minor": 1000, "reference": "FAKE-001"}, "LAB-ONLY")
        return {"http_status_simulated": status, "body": body}
    if which == "TC-03":
        return {"initial": "RECEIVED", "next": tc03_transition("RECEIVED", "UNKNOWN")}
    if which == "TC-04":
        ledger = SyntheticLedger()
        created = ledger.transfer("LAB-001", "FAKE-A", "FAKE-B", 1000)
        duplicate = ledger.transfer("LAB-001", "FAKE-A", "FAKE-B", 1000)
        return {"created": created, "duplicate_applied": duplicate,
                "balances": ledger.balances, "balanced": ledger.balanced()}
    if which == "TC-05":
        return {"allowed": tc05_authorize("payment:write", "LAB-ROLE:writer"),
                "denied": tc05_authorize("payment:write", "LAB-ROLE:reader"),
                "sanitized_log": tc05_redact({"event": "simulated_request",
                                              "correlation_id": "LAB-TRACE-01",
                                              "secret": "DO-NOT-LOG"})}
    if which == "TC-06":
        state, action = tc06_resolve("RECEIVED", None)
        return {"state": state, "next_action": action}
    if which == "TC-07":
        return tc07_review()
    raise ValueError(f"unknown lab: {which}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Offline OSEF training labs — synthetic data only")
    parser.add_argument("lab", choices=[f"TC-{i:02}" for i in range(1, 8)])
    args = parser.parse_args()
    print(json.dumps(run(args.lab), ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
