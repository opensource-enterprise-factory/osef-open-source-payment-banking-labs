#!/usr/bin/env python3
"""Unit tests: D02 Tazama reader is deterministic and never reaches the network."""
import importlib.util
import json
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "tazama-read-only-dry-run.py"
spec = importlib.util.spec_from_file_location("osef_tazama_reader", SCRIPT)
reader = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reader)
MSGID = "a21c6eb6dc8c4c56b4efcaf079b315ce"


def nalt():
    return {"message": "Report was found", "data": {"report": {
        "status": "NALT",
        "tadpResult": {"typologyResult": [{"result": 200,
                                           "workflow": {"alertThreshold": 300}}]},
    }, "dataCache": {"dbtrAcctId": "sensitive-placeholder", "instdAmt": {"amt": 370}}}}


class D02Tests(unittest.TestCase):
    def test_nalt_does_not_publish(self):
        result = reader.inspect_message(MSGID, fetch_once=lambda _: (200, nalt()))
        self.assertEqual(result, {"decision": "NO_PUBLISH", "reason": "NALT"})

    def test_retry_204_before_200(self):
        codes = iter([(204, None), (204, None), (200, nalt())])
        count = []
        result = reader.inspect_message(MSGID, fetch_once=lambda _: next(codes),
                                        sleep=lambda delay: count.append(delay))
        self.assertEqual(result["reason"], "NALT")
        self.assertEqual(count, [1, 1])

    def test_204_exhaustion(self):
        result = reader.inspect_message(MSGID, fetch_once=lambda _: (204, None),
                                        sleep=lambda _: None, attempts=2)
        self.assertEqual(result["reason"], "REPORT_NOT_READY")

    def test_401_no_retry(self):
        calls = []
        def fetch(_):
            calls.append(1)
            return 401, None
        result = reader.inspect_message(MSGID, fetch_once=fetch,
                                        sleep=lambda _: self.fail("must not sleep"))
        self.assertEqual(result["reason"], "SOURCE_HTTP_ERROR")
        self.assertEqual(len(calls), 1)

    def test_timeout_no_retry(self):
        result = reader.inspect_message(MSGID, fetch_once=lambda _: (0, None))
        self.assertEqual(result["decision"], "NO_PUBLISH")

    def test_positive_unapproved(self):
        payload = nalt()
        payload["data"]["report"]["status"] = "ALERT"
        result = reader.inspect_message(MSGID, fetch_once=lambda _: (200, payload))
        self.assertEqual(result["reason"], "UNAPPROVED_STATUS")

    def test_invalid_id_no_network(self):
        for msgid in ("", "https://evil.invalid", "../etc/passwd", "z" * 32, "f" * 33):
            with self.subTest(msgid=msgid):
                result = reader.inspect_message(msgid,
                    fetch_once=lambda _: self.fail("must not call network"))
                self.assertEqual(result["reason"], "INVALID_MESSAGE_ID")

    def test_no_sensitive_output(self):
        result = reader.inspect_message(MSGID, fetch_once=lambda _: (200, nalt()))
        serialized = json.dumps(result)
        for secret in (MSGID, "sensitive-placeholder", "370"):
            self.assertNotIn(secret, serialized)

    def test_invalid_attempts(self):
        result = reader.inspect_message(MSGID, attempts=100,
            fetch_once=lambda _: self.fail("must not call network"))
        self.assertEqual(result["reason"], "INVALID_ATTEMPTS")


if __name__ == "__main__":
    unittest.main()
