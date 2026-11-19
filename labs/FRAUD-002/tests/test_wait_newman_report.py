"""Unit tests: no network, no sleeps; ensure bounded polling and no false READY."""
import importlib.util
import unittest
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "scripts" / "wait-tazama-newman-report.py"
spec = importlib.util.spec_from_file_location("osef_wait_newman", PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
MSGID = "a8a4d16c08dc481ba85092c9abf895a4"


def valid():
    return {
        "data": {
            "transactionID": MSGID,
            "transaction": {"FIToFIPmtSts": {"GrpHdr": {"MsgId": MSGID}}},
            "report": {"status": "NALT"},
        }
    }


class ReadinessTest(unittest.TestCase):
    def test_extract_msgid(self):
        globals_ = {"values": [{"key": "messageIdPacs002", "value": MSGID, "enabled": True}]}
        self.assertEqual(mod.message_id_from_globals(globals_), MSGID)

    def test_reject_duplicate_id(self):
        globals_ = {"values": [
            {"key": "messageIdPacs002", "value": MSGID},
            {"key": "messageIdPacs002", "value": MSGID}]}
        with self.assertRaises(ValueError):
            mod.message_id_from_globals(globals_)

    def test_reject_invalid_or_missing_id(self):
        for value in ("bad", "", None, MSGID + "0"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    mod.message_id_from_globals({"values": [
                        {"key": "messageIdPacs002", "value": value}]})
        with self.assertRaises(ValueError):
            mod.message_id_from_globals({"values": []})

    def test_204_then_200(self):
        sequence = iter([(204, None), (204, None), (200, valid())])
        sleeps = []
        self.assertEqual(mod.wait_until_report(MSGID, fetch=lambda _: next(sequence),
                                               sleep=sleeps.append, attempts=3, interval=0.5),
                         "READY")
        self.assertEqual(sleeps, [0.5, 0.5])

    def test_no_ready_after_bound(self):
        calls = []
        with self.assertRaisesRegex(RuntimeError, "REPORT_NOT_READY"):
            mod.wait_until_report(MSGID, fetch=lambda _: (calls.append(1) or 204, None),
                                  sleep=lambda _: None, attempts=3)
        self.assertEqual(len(calls), 3)

    def test_wrong_status_immediate_stop(self):
        for status in (0, 401, 500):
            with self.subTest(status=status):
                with self.assertRaisesRegex(RuntimeError, "ADMIN_HTTP_ERROR"):
                    mod.wait_until_report(MSGID, fetch=lambda _: (status, None),
                                          sleep=lambda _: self.fail("unexpected retry"))

    def test_bad_body_rejected(self):
        for report in (None, {}, {"data": None}, {"data": {"report": None}}):
            with self.subTest(report=report):
                with self.assertRaises(RuntimeError):
                    mod.wait_until_report(MSGID, fetch=lambda _: (200, report),
                                          sleep=lambda _: self.fail("unexpected retry"))

    def test_wrong_identity_rejected(self):
        r = valid()
        r["data"]["transactionID"] = "f" * 32
        with self.assertRaisesRegex(RuntimeError, "MISMATCH"):
            mod.wait_until_report(MSGID, fetch=lambda _: (200, r))

    def test_wrong_pacs_msgid_rejected(self):
        r = valid()
        r["data"]["transaction"]["FIToFIPmtSts"]["GrpHdr"]["MsgId"] = "f" * 32
        with self.assertRaisesRegex(RuntimeError, "MISMATCH"):
            mod.wait_until_report(MSGID, fetch=lambda _: (200, r))

    def test_invalid_attempts(self):
        for attempts in (0, 61):
            with self.assertRaises(ValueError):
                mod.wait_until_report(MSGID, fetch=lambda _: self.fail("network"),
                                      attempts=attempts)

    def test_nalt_valid_readiness_without_publication(self):
        # A NALT report is ready for the upstream NALT assertions; this helper
        # does not make the decision to send any signal.
        self.assertEqual(mod.wait_until_report(MSGID, fetch=lambda _: (200, valid())),
                         "READY")


if __name__ == "__main__":
    unittest.main()
