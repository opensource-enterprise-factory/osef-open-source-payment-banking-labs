#!/usr/bin/env python3
"""E05: the direct bridge uses injected GET/POST; all tests are network-free."""
import importlib.util
import unittest
from pathlib import Path

DIR = Path(__file__).resolve().parents[1] / "scripts"
spec = importlib.util.spec_from_file_location("osef_e05_bridge", DIR / "tazama-direct-lab-submit.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
from test_signal_preview import alert, MSGID, KEY
from test_controlled_submit import POLICY, LAB_KEY


class E05DirectBridgeTests(unittest.TestCase):
    def test_valid_alrt_read_only_preview(self):
        r = mod.process_message(MSGID, POLICY, KEY, "", fetch=lambda _: (200, alert()))
        self.assertEqual(r, {"decision": "PREVIEW_ONLY", "reason": "SEND_NOT_ENABLED"})

    def test_actual_in_memory_full_path_with_mocks(self):
        observed = {}
        def post(p, k):
            self.assertEqual(k, LAB_KEY)
            observed.update(p)
            return 201, None
        def get(k):
            return 200, {"signals": [dict(observed)]}
        r = mod.process_message(MSGID, POLICY, KEY, LAB_KEY, enabled=True,
                                fetch=lambda _: (200, alert()), submit=(post, get))
        self.assertEqual(r, {"decision": "SENT_AND_RECEIVED", "reason": "PSP_B_CONFIRMED"})
        self.assertNotIn(MSGID, str(observed))
        self.assertNotIn("DO-NOT-SHARE", str(observed))

    def test_nalt_blocks_post(self):
        p = alert()
        p["data"]["report"]["status"] = "NALT"
        r = mod.process_message(MSGID, POLICY, KEY, LAB_KEY, enabled=True,
                                fetch=lambda _: (200, p),
                                submit=(lambda *a: self.fail("POST forbidden"),
                                        lambda *a: self.fail("GET receipt forbidden")))
        self.assertEqual(r["decision"], "NO_SEND")

    def test_report_id_mismatch_blocks_post(self):
        r = mod.process_message(MSGID, POLICY, KEY, LAB_KEY, enabled=True,
                                fetch=lambda _: (200, alert("f" * 32)),
                                submit=(lambda *a: self.fail("POST forbidden"),
                                        lambda *a: self.fail("GET receipt forbidden")))
        self.assertEqual(r["reason"], "MESSAGE_ID_MISMATCH")

    def test_missing_approval_does_not_even_read(self):
        p = dict(POLICY, approved_for_lab=False)
        r = mod.process_message(MSGID, p, KEY, LAB_KEY, enabled=True,
                                fetch=lambda _: self.fail("Tazama GET forbidden"))
        self.assertEqual(r["reason"], "POLICY_NOT_REVIEWED")

    def test_policy_mismatch_does_not_read(self):
        p = dict(POLICY, severity="high")
        r = mod.process_message(MSGID, p, KEY, LAB_KEY, enabled=True,
                                fetch=lambda _: self.fail("Tazama GET forbidden"))
        self.assertEqual(r["reason"], "POLICY_NOT_REVIEWED")

    def test_invalid_id_does_not_read(self):
        r = mod.process_message("not-a-msgid", POLICY, KEY, LAB_KEY,
                                fetch=lambda _: self.fail("Tazama GET forbidden"))
        self.assertEqual(r["reason"], "INVALID_MESSAGE_ID")

    def test_missing_lab_key_does_not_read_for_send(self):
        r = mod.process_message(MSGID, POLICY, KEY, "", enabled=True,
                                fetch=lambda _: self.fail("Tazama GET forbidden"))
        self.assertEqual(r["reason"], "MISSING_PSP_LAB_KEY")

    def test_missing_token_key_does_not_read(self):
        r = mod.process_message(MSGID, POLICY, "", LAB_KEY, enabled=True,
                                fetch=lambda _: self.fail("Tazama GET forbidden"))
        self.assertEqual(r["reason"], "MISSING_LAB_TOKEN_KEY")

    def test_http_204_401_503_fail_closed(self):
        for status, expected in ((204, "TAZAMA_NOT_READY"),
                                 (401, "TAZAMA_UNAVAILABLE"),
                                 (503, "TAZAMA_UNAVAILABLE")):
            with self.subTest(status=status):
                r = mod.process_message(MSGID, POLICY, KEY, LAB_KEY,
                                        fetch=lambda _: (status, None))
                self.assertEqual(r["reason"], expected)

    def test_fetch_error_fail_closed(self):
        def failing(_):
            raise TimeoutError()
        r = mod.process_message(MSGID, POLICY, KEY, LAB_KEY, fetch=failing)
        self.assertEqual(r["decision"], "NO_SEND")

    def test_http_200_invalid_payload(self):
        r = mod.process_message(MSGID, POLICY, KEY, LAB_KEY,
                                fetch=lambda _: (200, {"message": "not a report"}))
        self.assertEqual(r["decision"], "NO_SEND")

    def test_report_kept_out_of_result(self):
        result = mod.process_message(MSGID, POLICY, KEY, LAB_KEY,
                                     fetch=lambda _: (200, alert()))
        self.assertNotIn("dataCache", str(result))
        self.assertNotIn(MSGID, str(result))
        self.assertNotIn("transaction_token", str(result))


if __name__ == "__main__":
    unittest.main()
