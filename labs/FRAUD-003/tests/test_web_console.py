"""Dashboard HTTP contract checks: no secrets rendered, API isolation intact."""
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


class WebConsoleTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.context = TestClient(
            create_app(db_path=str(Path(self.temp.name) / "demo.db"), keys=KEYS)
        )
        self.client = self.context.__enter__()
        self.addCleanup(self.context.__exit__, None, None, None)

    def test_dashboard_renders_without_credentials(self):
        resp = self.client.get("/")
        self.assertEqual(200, resp.status_code)
        self.assertIn("text/html", resp.headers["content-type"])
        self.assertIn("no-store", resp.headers["cache-control"])
        self.assertIn("frame-ancestors 'none'", resp.headers["content-security-policy"])
        self.assertIn('src="/ui.js"', resp.text)
        self.assertIn("Banque A", resp.text)
        self.assertIn("Mobile Money C", resp.text)
        for secret in KEYS.values():
            self.assertNotIn(secret, resp.text)

    def test_dashboard_javascript_not_cached_or_secret_bearing(self):
        resp = self.client.get("/ui.js")
        self.assertEqual(200, resp.status_code)
        self.assertIn("javascript", resp.headers["content-type"])
        self.assertIn("no-store", resp.headers["cache-control"])
        self.assertIn("credentials:\"omit\"", resp.text)
        self.assertIn("session navigateur", resp.text)
        self.assertNotIn("localStorage", resp.text.replace("No localStorage", ""))
        for secret in KEYS.values():
            self.assertNotIn(secret, resp.text)

    def test_dashboard_does_not_make_api_public(self):
        self.assertEqual(401, self.client.get("/signals").status_code)

    def test_dashboard_not_in_openapi_contract(self):
        paths = self.client.get("/openapi.json").json()["paths"]
        self.assertNotIn("/", paths)
        self.assertNotIn("/ui.js", paths)


if __name__ == "__main__":
    unittest.main()
