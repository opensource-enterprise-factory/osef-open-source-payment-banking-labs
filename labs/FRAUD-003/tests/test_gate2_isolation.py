"""Gate 2 regression tests — in-memory HTTP calls, no Docker or external networks."""
import os
import sys
import tempfile
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import create_app

KEYS = {
    "demo-bank-a": "A" * 48,
    "demo-psp-b": "B" * 48,
    "demo-mobile-c": "C" * 48,
}


def payload(signal_id="demo-signal-00000001", **changes):
    data = {
        "signal_id": signal_id,
        "category": "suspicious-transfer",
        "severity": "medium",
        "scenario_ref": "demo-scenario-00000001",
        "expires_in_hours": 1,
    }
    data.update(changes)
    return data


def headers(institution):
    return {"X-Lab-Key": KEYS[institution]}


class Gate2IsolationTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.client_context = TestClient(
            create_app(db_path=str(Path(self.tmp.name) / "signals.db"), keys=KEYS)
        )
        self.client = self.client_context.__enter__()
        self.addCleanup(self.client_context.__exit__, None, None, None)

    def test_health(self):
        self.assertEqual(200, self.client.get("/health").status_code)

    def test_all_three_institutions_create_and_read_only_own(self):
        institutions = list(KEYS)
        for n, institution in enumerate(institutions):
            res = self.client.post(
                "/signals",
                json=payload(f"demo-signal-0000000{n+1}"),
                headers=headers(institution),
            )
            self.assertEqual(201, res.status_code)
        for n, institution in enumerate(institutions):
            own = self.client.get("/signals", headers=headers(institution))
            self.assertEqual(200, own.status_code)
            self.assertEqual(institution, own.json()["institution"])
            self.assertEqual(
                [f"demo-signal-0000000{n+1}"],
                [item["signal_id"] for item in own.json()["signals"]],
            )
            other = (n + 1) % 3
            denied = self.client.get(
                f"/signals/demo-signal-0000000{other+1}",
                headers=headers(institution),
            )
            self.assertEqual(404, denied.status_code)

    def test_no_credentials_or_bad_key(self):
        self.assertEqual(401, self.client.get("/signals").status_code)
        self.assertEqual(
            401, self.client.post("/signals", json=payload(), headers={"X-Lab-Key": "bad"}).status_code
        )

    def test_duplicate_within_institution_not_across_institutions(self):
        self.assertEqual(
            201, self.client.post("/signals", json=payload(), headers=headers("demo-bank-a")).status_code
        )
        self.assertEqual(
            409, self.client.post("/signals", json=payload(), headers=headers("demo-bank-a")).status_code
        )
        self.assertEqual(
            201, self.client.post("/signals", json=payload(), headers=headers("demo-psp-b")).status_code
        )

    def test_payload_unknown_or_sensitive_fields_rejected(self):
        self.assertEqual(
            422,
            self.client.post("/signals", json=payload(pan="4111111111111111"), headers=headers("demo-bank-a")).status_code,
        )

    def test_invalid_identifiers_and_ttl_rejected(self):
        for body in [payload(signal_id="real-client-1234"), payload(expires_in_hours=0),
                     payload(expires_in_hours=25), payload(scenario_ref="client-private")]:
            with self.subTest(body=body):
                self.assertEqual(
                    422, self.client.post("/signals", json=body, headers=headers("demo-bank-a")).status_code
                )

    def test_expired_signal_not_visible(self):
        self.assertEqual(
            201, self.client.post("/signals", json=payload(), headers=headers("demo-bank-a")).status_code
        )
        import sqlite3
        with sqlite3.connect(str(Path(self.tmp.name) / "signals.db")) as db:
            db.execute("UPDATE signals SET expires_at=? WHERE institution=?", (
                "2000-01-01T00:00:00+00:00", "demo-bank-a"
            ))
        self.assertEqual([], self.client.get("/signals", headers=headers("demo-bank-a")).json()["signals"])
        self.assertEqual(
            404, self.client.get("/signals/demo-signal-00000001", headers=headers("demo-bank-a")).status_code
        )

    def test_non_distinct_or_missing_keys_fail_closed(self):
        with self.assertRaisesRegex(RuntimeError, "distinct"):
            with TestClient(create_app(db_path=str(Path(self.tmp.name) / "bad.db"),
                                           keys={k: "A"*48 for k in KEYS})):
                pass
        with self.assertRaisesRegex(RuntimeError, "distinct"):
            with TestClient(create_app(db_path=str(Path(self.tmp.name) / "bad2.db"),
                                           keys={k: "" for k in KEYS})):
                pass


if __name__ == "__main__":
    unittest.main()
