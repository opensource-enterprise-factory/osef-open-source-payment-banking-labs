#!/usr/bin/env python3
"""FRAUD-002 D02: read Tazama Admin report on loopback, never publish signals.

Sandbox-only client. No secrets, no mutating HTTP, no direct database access.
The response is processed in memory; stdout contains ONLY a minimal decision.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE_URL = "http://127.0.0.1:5100"
REPORT_ENDPOINT = "/v1/admin/reports/getreportbymsgid"
ID_PATTERN = re.compile(r"^[a-fA-F0-9]{32}$")
MAX_BODY_BYTES = 1_048_576
TIMEOUT_SECONDS = 5
MAX_ATTEMPTS = 4
RETRY_DELAY_SECONDS = 1
CLASSIFIER_PATH = Path(__file__).with_name("tazama-adapter-dry-run.py")


def _load_classifier():
    spec = importlib.util.spec_from_file_location("osef_tazama_offline_classifier", CLASSIFIER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("classifier unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.assess_report


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """Refuse to follow redirects, including to non-loopback destinations."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def _fetch_once(message_id: str, *, open_url=None) -> tuple[int, object | None]:
    # Constant, hardcoded loopback target: no user-supplied host, redirect, auth or headers.
    url = BASE_URL + REPORT_ENDPOINT + "?" + urllib.parse.urlencode({"msgid": message_id})
    request = urllib.request.Request(url, method="GET")
    if open_url is None:
        # Disable proxy environment inheritance and redirects.
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), _NoRedirect())
        open_url = opener.open
    try:
        with open_url(request, timeout=TIMEOUT_SECONDS) as response:
            # Reject redirects, including redirects off loopback.
            if response.geturl() != url:
                return 0, None
            code = response.status
            if code == 204:
                return 204, None
            if code != 200:
                return code, None
            body = response.read(MAX_BODY_BYTES + 1)
            if len(body) > MAX_BODY_BYTES:
                return 0, None
            try:
                payload = json.loads(body)
            except (ValueError, UnicodeError):
                return 0, None
            return 200, payload
    except urllib.error.HTTPError as exc:
        # No sensitive response body or headers in logs.
        exc.close()
        return exc.code, None
    except (urllib.error.URLError, socket.timeout, TimeoutError, ConnectionError, OSError):
        return 0, None


def inspect_message(message_id: str, *, fetch_once=_fetch_once, sleep=time.sleep,
                    attempts: int = MAX_ATTEMPTS) -> dict[str, str]:
    if not ID_PATTERN.fullmatch(message_id):
        return {"decision": "NO_PUBLISH", "reason": "INVALID_MESSAGE_ID"}
    if not 1 <= attempts <= MAX_ATTEMPTS:
        return {"decision": "NO_PUBLISH", "reason": "INVALID_ATTEMPTS"}
    classify = _load_classifier()
    for index in range(attempts):
        code, payload = fetch_once(message_id)
        if code == 204:
            if index + 1 < attempts:
                sleep(RETRY_DELAY_SECONDS)
                continue
            return classify(None, http_status=204)
        if code != 200:
            return {"decision": "NO_PUBLISH", "reason": "SOURCE_HTTP_ERROR"}
        # Never print payload / IDs. A qualified ALRT is review-only, never sent.
        return classify(payload, http_status=200)
    return {"decision": "NO_PUBLISH", "reason": "REPORT_NOT_READY"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Tazama Admin loopback-only read-only dry-run")
    parser.add_argument("--msgid", required=True, help="32-character hexadecimal synthetic lab message ID")
    parser.add_argument("--attempts", type=int, choices=range(1, MAX_ATTEMPTS + 1),
                        default=MAX_ATTEMPTS, metavar="1..4")
    args = parser.parse_args()
    result = inspect_message(args.msgid, attempts=args.attempts)
    print(json.dumps(result, sort_keys=True))
    return 0 if result["reason"] in ("NALT", "REPORT_NOT_READY") else 2


if __name__ == "__main__":
    raise SystemExit(main())
