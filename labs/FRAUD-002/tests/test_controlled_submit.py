#!/usr/bin/env python3
"""Gate D06-2 network harness tests use injected mocks, never real network."""
import importlib.util
import unittest
from pathlib import Path

DIR = Path(__file__).resolve().parents[1] / "scripts"
spec = importlib.util.spec_from_file_location("osef_d06_submit", DIR / "tazama-controlled-submit.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
from test_signal_preview import alert, MSGID, KEY

POLICY = {
    "approved_for_lab": True,
    "approval_reference": "OSEF-D06-LAB-20261119",
    "category": "suspicious-transfer",
    "severity": "medium",
    "recipient": "psp-b",
    "expires_in_hours": 1,
}
LAB_KEY = "synthetic-test-lab-user-secret-12345678"


class GateD06ControlledSubmitTests(unittest.TestCase):
    def test_default_off_does_not_call_network(self):
        def never(*a):
            raise AssertionError("network must not be called")
        r = module.execute(alert(), MSGID, POLICY, KEY, LAB_KEY, post=never, get=never)
        self.assertEqual(r["decision"], "PREVIEW_ONLY")

    def test_no_policy_no_network(self):
        r = module.execute(alert(), MSGID, {}, KEY, LAB_KEY, enabled=True,
                           post=lambda *a: self.fail("unexpected HTTP"))
        self.assertEqual(r["reason"], "POLICY_NOT_REVIEWED")

    def test_no_approval_flag_no_network(self):
        p = dict(POLICY, approved_for_lab=False)
        r = module.execute(alert(), MSGID, p, KEY, LAB_KEY, enabled=True,
                           post=lambda *a: self.fail("unexpected HTTP"))
        self.assertEqual(r["decision"], "NO_SEND")

    def test_no_arbitrary_severity(self):
        p = dict(POLICY, severity="high")
        r = module.execute(alert(), MSGID, p, KEY, LAB_KEY, enabled=True,
                           post=lambda *a: self.fail("unexpected HTTP"))
        self.assertEqual(r["reason"], "POLICY_MISMATCH")

    def test_no_nalt(self):
        p = alert()
        p["data"]["report"]["status"] = "NALT"
        r = module.execute(p, MSGID, POLICY, KEY, LAB_KEY, enabled=True,
                           post=lambda *a: self.fail("unexpected HTTP"))
        self.assertEqual(r["decision"], "NO_SEND")

    def test_no_invalid_id_binding(self):
        r = module.execute(alert(), "f" * 32, POLICY, KEY, LAB_KEY, enabled=True,
                           post=lambda *a: self.fail("unexpected HTTP"))
        self.assertEqual(r["decision"], "NO_SEND")

    def test_send_and_receive_through_mocks(self):
        recorded = {}
        def post(p, k):
            recorded.update(p)
            self.assertEqual(k, LAB_KEY)
            return 201, {"status": "accepted"}
        def get(k):
            self.assertEqual(k, LAB_KEY)
            return 200, {"signals": [dict(recorded)]}
        r = module.execute(alert(), MSGID, POLICY, KEY, LAB_KEY,
                           enabled=True, post=post, get=get)
        self.assertEqual(r, {"decision": "SENT_AND_RECEIVED", "reason": "PSP_B_CONFIRMED"})
        self.assertEqual(set(recorded), {"transaction_token", "category", "severity",
                                        "recipient", "expires_in_hours"})

    def test_duplicate_409_no_receipt_read(self):
        r = module.execute(alert(), MSGID, POLICY, KEY, LAB_KEY, enabled=True,
                           post=lambda p, k: (409, None),
                           get=lambda k: self.fail("must not read after duplicate"))
        self.assertEqual(r, {"decision": "DUPLICATE", "reason": "PSP_A_409"})

    def test_401_503_and_unexpected(self):
        for status, reason in [(401, "PSP_A_UNAUTHORIZED"), (503, "PSP_A_UNAVAILABLE"),
                               (0, "PSP_A_UNAVAILABLE"), (502, "PSP_A_REJECTED"),
                               (200, "PSP_A_REJECTED")]:
            with self.subTest(status=status):
                r = module.execute(alert(), MSGID, POLICY, KEY, LAB_KEY,
                                   enabled=True, post=lambda p, k: (status, None),
                                   get=lambda k: self.fail("unexpected receipt read"))
                self.assertEqual(r["reason"], reason)

    def test_201_without_receipt_confirmation_is_not_success(self):
        r = module.execute(alert(), MSGID, POLICY, KEY, LAB_KEY, enabled=True,
                           post=lambda p, k: (201, None), get=lambda k: (503, None))
        self.assertEqual(r, {"decision": "SENT", "reason": "RECEIPT_UNCONFIRMED"})

    def test_missing_lab_key_no_network(self):
        r = module.execute(alert(), MSGID, POLICY, KEY, "", enabled=True,
                           post=lambda *a: self.fail("unexpected HTTP"))
        self.assertEqual(r["reason"], "MISSING_PSP_LAB_KEY")

    def test_read_only_sources_and_exact_urls(self):
        self.assertEqual(module.PSP_A_URL, "http://127.0.0.1:8091/submit")
        self.assertEqual(module.PSP_B_URL, "http://127.0.0.1:8092/inbox")


if __name__ == "__main__":
    unittest.main()
