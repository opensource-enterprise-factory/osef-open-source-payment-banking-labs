#!/usr/bin/env python3
"""D06-1: no network, approved lab-only signal preview and minimum disclosure."""
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "scripts"
spec = importlib.util.spec_from_file_location("osef_d06_preview", ROOT / "tazama-signal-preview.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
MSGID = "a8a4d16c08dc481ba85092c9abf895a4"
KEY = "a-fixed-strong-secret-key-for-synthetic-tests-12345"
POLICY = {
    "approved_for_lab": True,
    "approval_reference": "OSEF-LAB-D06-REVIEW",
    "category": "suspicious-transfer",
    "severity": "medium",  # Test fixture only; no real mapping approval implied.
    "recipient": "psp-b",
    "expires_in_hours": 1,
}


def alert(msgid=MSGID):
    return {
        "message": "Report was found",
        "data": {
            "transactionID": msgid,
            "report": {
                "status": "ALRT",
                "tadpResult": {"typologyResult": [{
                    "cfg": "999-901-902@4.0.0",
                    "result": 600,
                    "workflow": {
                        "alertThreshold": 300,
                        "interdictionThreshold": 500,
                        "flowProcessor": "EFRuP@4.0.0",
                    },
                    "ruleResults": [
                        {"id": "901@4.0.0", "subRuleRef": ".03", "wght": 400},
                        {"id": "902@4.0.0", "subRuleRef": ".02", "wght": 200},
                        {"id": "EFRuP@4.0.0", "subRuleRef": "none", "wght": 0},
                    ],
                }]},
            },
            "transaction": {
                "FIToFIPmtSts": {"GrpHdr": {"MsgId": msgid}},
                "DataCache": {"dbtrAcctId": "DO-NOT-SHARE", "instdAmt": {"amt": 730}},
            },
        },
    }


class GateD06PreviewTests(unittest.TestCase):
    def test_approved_lab_preview(self):
        r = mod.prepare_signal(alert(), MSGID, POLICY, KEY)
        self.assertEqual(r["decision"], "PREVIEW_ONLY")
        self.assertEqual(set(r["signal"]), {"transaction_token", "category",
                         "severity", "recipient", "expires_in_hours"})
        self.assertRegex(r["signal"]["transaction_token"], r"^demo-[0-9a-f]{32}$")

    def test_no_sensitive_data_leakage(self):
        r = mod.prepare_signal(alert(), MSGID, POLICY, KEY)
        output = json.dumps(r)
        for item in ("DO-NOT-SHARE", "730", MSGID, "dbtrAcctId", "instdAmt"):
            self.assertNotIn(item, output)

    def test_stable_on_retry(self):
        a = mod.prepare_signal(alert(), MSGID, POLICY, KEY)
        b = mod.prepare_signal(alert(), MSGID, POLICY, KEY)
        self.assertEqual(a["signal"]["transaction_token"], b["signal"]["transaction_token"])

    def test_secret_is_domain_separated(self):
        a = mod.prepare_signal(alert(), MSGID, POLICY, KEY)
        b = mod.prepare_signal(alert(), MSGID, POLICY, KEY + "another")
        self.assertNotEqual(a["signal"]["transaction_token"], b["signal"]["transaction_token"])

    def test_nalt_never_published(self):
        p = alert()
        p["data"]["report"]["status"] = "NALT"
        self.assertEqual(mod.prepare_signal(p, MSGID, POLICY, KEY)["decision"], "NO_PUBLISH")

    def test_missing_policy(self):
        self.assertEqual(mod.prepare_signal(alert(), MSGID, None, KEY)["reason"], "UNAPPROVED_POLICY")

    def test_approval_required(self):
        p = dict(POLICY, approved_for_lab=False)
        self.assertEqual(mod.prepare_signal(alert(), MSGID, p, KEY)["reason"], "UNAPPROVED_POLICY")

    def test_severity_not_inferred(self):
        p = dict(POLICY)
        p.pop("severity")
        self.assertEqual(mod.prepare_signal(alert(), MSGID, p, KEY)["reason"], "INVALID_POLICY")

    def test_invalid_ttl(self):
        for v in (0, 25, True, "1"):
            with self.subTest(v=v):
                p = dict(POLICY, expires_in_hours=v)
                self.assertEqual(mod.prepare_signal(alert(), MSGID, p, KEY)["reason"], "INVALID_POLICY")

    def test_wrong_recipient(self):
        p = dict(POLICY, recipient="psp-a")
        self.assertEqual(mod.prepare_signal(alert(), MSGID, p, KEY)["reason"], "INVALID_POLICY")

    def test_short_secret(self):
        self.assertEqual(mod.prepare_signal(alert(), MSGID, POLICY, "short")["reason"], "MISSING_LAB_KEY")

    def test_mismatched_report_id(self):
        p = alert()
        p["data"]["transactionID"] = "f" * 32
        self.assertEqual(mod.prepare_signal(p, MSGID, POLICY, KEY)["reason"], "MESSAGE_ID_MISMATCH")

    def test_mismatched_pacs002_id(self):
        p = alert()
        p["data"]["transaction"]["FIToFIPmtSts"]["GrpHdr"]["MsgId"] = "f" * 32
        self.assertEqual(mod.prepare_signal(p, MSGID, POLICY, KEY)["reason"], "MESSAGE_ID_MISMATCH")

    def test_unknown_rule(self):
        p = alert()
        p["data"]["report"]["tadpResult"]["typologyResult"][0]["ruleResults"][0]["wght"] = 900
        self.assertEqual(mod.prepare_signal(p, MSGID, POLICY, KEY)["reason"], "REPORT_NOT_QUALIFIED")

    def test_204_report(self):
        self.assertEqual(mod.prepare_signal({}, MSGID, POLICY, KEY)["decision"], "NO_PUBLISH")


if __name__ == "__main__":
    unittest.main()
