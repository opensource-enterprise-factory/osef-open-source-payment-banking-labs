"""Regression tests for all seven synthetic OSEF Academy core labs."""
import unittest
from runner import (SyntheticLedger, run, tc01_manifest, tc02_api,
                    tc03_transition, tc05_authorize, tc05_redact, tc06_resolve,
                    tc07_review)


class CommonCoreTests(unittest.TestCase):
    def test_every_lab_returns_demo_output(self):
        for number in range(1, 8):
            with self.subTest(lab=number):
                self.assertIsInstance(run(f"TC-{number:02}"), dict)

    def test_tc01_deterministic_manifest(self):
        self.assertEqual(tc01_manifest(), tc01_manifest())
        self.assertEqual(len(tc01_manifest()["sha256"]), 64)

    def test_tc02_positive_and_access_controls(self):
        valid = {"reference": "FAKE-001", "amount_minor": 1000}
        self.assertEqual(tc02_api("POST", "/fake-payments", valid, "LAB-ONLY")[0], 201)
        self.assertEqual(tc02_api("POST", "/fake-payments", valid, "BAD")[0], 401)
        self.assertEqual(tc02_api("POST", "/wrong", valid, "LAB-ONLY")[0], 404)

    def test_tc02_invalid_payload(self):
        for payload in ({}, {"reference": "FAKE-01", "amount_minor": -1},
                        {"reference": "REAL-01", "amount_minor": 20},
                        {"reference": "FAKE-01", "amount_minor": True}):
            with self.subTest(payload=payload):
                self.assertEqual(tc02_api("POST", "/fake-payments", payload, "LAB-ONLY")[0], 422)

    def test_tc03_unknown_is_distinct_from_decline(self):
        self.assertEqual(tc03_transition("RECEIVED", "UNKNOWN"), "UNKNOWN")
        self.assertEqual(tc03_transition("UNKNOWN", "APPROVED"), "APPROVED")
        with self.assertRaises(ValueError):
            tc03_transition("APPROVED", "DECLINED")

    def test_tc04_ledger_is_balanced_and_idempotent(self):
        ledger = SyntheticLedger()
        self.assertTrue(ledger.transfer("LAB-A", "FAKE-A", "FAKE-B", 200))
        self.assertFalse(ledger.transfer("LAB-A", "FAKE-A", "FAKE-B", 200))
        self.assertTrue(ledger.balanced())
        self.assertEqual(ledger.balances["FAKE-A"], 9800)
        self.assertEqual(len(ledger.journal), 2)
        with self.assertRaises(ValueError):
            ledger.transfer("LAB-A", "FAKE-A", "FAKE-B", 201)

    def test_tc04_invalid_transfers_leave_state_unchanged(self):
        ledger = SyntheticLedger()
        for bad in (0, -2, True, 10001):
            with self.subTest(amount=bad):
                with self.assertRaises(ValueError):
                    ledger.transfer("LAB-X", "FAKE-A", "FAKE-B", bad)
        self.assertEqual(ledger.balances, {"FAKE-A": 10000, "FAKE-B": 0})
        self.assertEqual(ledger.journal, [])

    def test_tc05_scope_and_redaction(self):
        self.assertTrue(tc05_authorize("payment:write", "LAB-ROLE:writer"))
        self.assertFalse(tc05_authorize("payment:write", "LAB-ROLE:reader"))
        self.assertFalse(tc05_authorize("payment:read", "LAB-ROLE:writer"))
        self.assertNotIn("secret", tc05_redact({"event": "fake", "secret": "LEAK"}))

    def test_tc06_timeout_is_unknown_not_declined(self):
        self.assertEqual(tc06_resolve("RECEIVED", None)[0], "UNKNOWN")
        self.assertEqual(tc06_resolve("RECEIVED", "ACCEPT")[0], "APPROVED")
        self.assertEqual(tc06_resolve("RECEIVED", "DECLINE")[0], "DECLINED")
        with self.assertRaises(ValueError):
            tc06_resolve("RECEIVED", "UNSUPPORTED")

    def test_tc07_has_four_architecture_layers(self):
        self.assertTrue({"business", "data", "application", "technology"}.issubset(tc07_review()))
        self.assertEqual(tc07_review()["status"], "conceptual_lab_only")


if __name__ == "__main__":
    unittest.main()
