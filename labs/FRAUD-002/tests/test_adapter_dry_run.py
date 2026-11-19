#!/usr/bin/env python3
"""Unit tests for FRAUD-002 Gate D offline classifier; no network calls."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "tazama-adapter-dry-run.py"
spec = importlib.util.spec_from_file_location("tazama_adapter_dry_run", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def report(status="NALT", score=200, threshold=300):
    return {
        "message": "Report was found",
        "data": {
            "report": {
                "status": status,
                "tadpResult": {"typologyResult": [
                    {"result": score, "workflow": {"alertThreshold": threshold}}
                ]},
            },
            "dataCache": {"instdAmt": {"amt": 370, "ccy": "USD"},
                          "dbtrAcctId": "FAKE-SENSITIVE-LAB-ACCOUNT"},
        },
    }


class GateDTests(unittest.TestCase):
    def test_nalt_even_with_nonzero_weights(self):
        self.assertEqual(module.assess_report(report()),
                         {"decision": "NO_PUBLISH", "reason": "NALT"})

    def test_nalt_even_if_score_inconsistent(self):
        self.assertEqual(module.assess_report(report(score=900))["reason"], "NALT")

    def test_http_204(self):
        self.assertEqual(module.assess_report(None, http_status=204)["reason"],
                         "REPORT_NOT_READY")

    def test_http_error(self):
        self.assertEqual(module.assess_report(report(), http_status=401)["reason"],
                         "SOURCE_HTTP_ERROR")

    def test_malformed(self):
        for payload in (None, [], {}, {"data": {}}, {"data": {"report": []}}):
            with self.subTest(payload=payload):
                self.assertEqual(module.assess_report(payload)["decision"], "NO_PUBLISH")

    def test_unconfirmed_message(self):
        value = report()
        value["message"] = "anything else"
        self.assertEqual(module.assess_report(value)["reason"], "UNCONFIRMED_REPORT")

    def test_unknown_status_even_with_high_score(self):
        self.assertEqual(module.assess_report(report(status="ALERT", score=900))["reason"],
                         "UNAPPROVED_STATUS")

    def test_no_sensitive_fields_in_output(self):
        output = json.dumps(module.assess_report(report()))
        self.assertNotIn("FAKE-SENSITIVE-LAB-ACCOUNT", output)
        self.assertNotIn("370", output)

    def test_cli_offline_fixture(self):
        with tempfile.TemporaryDirectory() as tmp:
            filename = Path(tmp) / "sanitized.json"
            filename.write_text(json.dumps(report()), encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), "--report", str(filename)],
                                    capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["reason"], "NALT")

    def test_cli_status_204_without_file(self):
        result = subprocess.run([sys.executable, str(SCRIPT), "--http-status", "204"],
                                capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["reason"], "REPORT_NOT_READY")


if __name__ == "__main__":
    unittest.main()
