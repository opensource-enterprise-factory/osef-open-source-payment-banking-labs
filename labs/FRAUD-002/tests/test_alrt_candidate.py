#!/usr/bin/env python3
"""Gate D05: qualified Tazama ALRT is review-only and never published."""
import importlib.util
import json
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


classifier = load("osef_d05_classifier", "tazama-adapter-dry-run.py")
reader = load("osef_d05_reader", "tazama-read-only-dry-run.py")
MSGID = "a8a4d16c08dc481ba85092c9abf895a4"


def positive():
    return {
        "message": "Report was found",
        "data": {
            "report": {
                "status": "ALRT",
                "tadpResult": {"typologyResult": [{
                    "cfg": "999-901-902@4.0.0",
                    "result": 600,
                    "workflow": {
                        "flowProcessor": "EFRuP@4.0.0",
                        "alertThreshold": 300,
                        "interdictionThreshold": 500,
                    },
                    "ruleResults": [
                        {"id": "EFRuP@4.0.0", "subRuleRef": "none", "wght": 0},
                        {"id": "902@4.0.0", "subRuleRef": ".02", "wght": 200},
                        {"id": "901@4.0.0", "subRuleRef": ".03", "wght": 400},
                    ],
                }]},
            },
            "dataCache": {
                "dbtrAcctId": "SENSITIVE-ACCOUNT-TEST",
                "instdAmt": {"amt": 730, "ccy": "USD"},
            },
        },
    }


class GateD05Tests(unittest.TestCase):
    def test_positive_from_observed_synthetic_profile_review_only(self):
        self.assertEqual(classifier.assess_report(positive()),
                         {"decision": "REVIEW_ONLY", "reason": "ALRT_CANDIDATE"})

    def test_reader_still_no_network_delivery(self):
        self.assertEqual(reader.inspect_message(MSGID, fetch_once=lambda _: (200, positive())),
                         {"decision": "REVIEW_ONLY", "reason": "ALRT_CANDIDATE"})

    def test_no_sensitive_output(self):
        output = json.dumps(classifier.assess_report(positive()))
        for forbidden in ("730", "SENSITIVE-ACCOUNT-TEST", MSGID,
                          "suspicious-transfer", "high", "psp-b"):
            self.assertNotIn(forbidden, output)

    def test_score_below_threshold(self):
        p = positive()
        p["data"]["report"]["tadpResult"]["typologyResult"][0]["result"] = 200
        self.assertEqual(classifier.assess_report(p)["reason"], "ALRT_NOT_QUALIFIED")

    def test_wrong_rule_weight(self):
        p = positive()
        p["data"]["report"]["tadpResult"]["typologyResult"][0]["ruleResults"][1]["wght"] = 800
        self.assertEqual(classifier.assess_report(p)["reason"], "ALRT_NOT_QUALIFIED")

    def test_extra_rule(self):
        p = positive()
        p["data"]["report"]["tadpResult"]["typologyResult"][0]["ruleResults"].append(
            {"id": "OTHER", "subRuleRef": ".01", "wght": 0})
        self.assertEqual(classifier.assess_report(p)["reason"], "ALRT_NOT_QUALIFIED")

    def test_duplicate_rule(self):
        p = positive()
        rules = p["data"]["report"]["tadpResult"]["typologyResult"][0]["ruleResults"]
        rules[0] = dict(rules[1])
        self.assertEqual(classifier.assess_report(p)["reason"], "ALRT_NOT_QUALIFIED")

    def test_unknown_typology(self):
        p = positive()
        p["data"]["report"]["tadpResult"]["typologyResult"][0]["cfg"] = "unknown"
        self.assertEqual(classifier.assess_report(p)["reason"], "ALRT_NOT_QUALIFIED")

    def test_wrong_threshold(self):
        p = positive()
        p["data"]["report"]["tadpResult"]["typologyResult"][0]["workflow"]["alertThreshold"] = 100
        self.assertEqual(classifier.assess_report(p)["reason"], "ALRT_NOT_QUALIFIED")

    def test_bool_not_number(self):
        p = positive()
        p["data"]["report"]["tadpResult"]["typologyResult"][0]["ruleResults"][1]["wght"] = True
        self.assertEqual(classifier.assess_report(p)["reason"], "ALRT_NOT_QUALIFIED")

    def test_missing_rules_and_malformed(self):
        for value in (None, {}, [], "not-a-list"):
            p = positive()
            p["data"]["report"]["tadpResult"]["typologyResult"][0]["ruleResults"] = value
            with self.subTest(value=value):
                self.assertEqual(classifier.assess_report(p)["reason"], "ALRT_NOT_QUALIFIED")

    def test_nalt_still_filtered(self):
        p = positive()
        p["data"]["report"]["status"] = "NALT"
        self.assertEqual(classifier.assess_report(p),
                         {"decision": "NO_PUBLISH", "reason": "NALT"})

    def test_204_and_401_still_filtered(self):
        self.assertEqual(classifier.assess_report(None, http_status=204)["decision"],
                         "NO_PUBLISH")
        self.assertEqual(classifier.assess_report(positive(), http_status=401)["decision"],
                         "NO_PUBLISH")


if __name__ == "__main__":
    unittest.main()
