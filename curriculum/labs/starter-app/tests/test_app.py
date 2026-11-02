"""Smoke tests for the Cloud Track demo API."""

import json
import os
import threading
import unittest
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from unittest.mock import patch

from app import RequestHandler


class AppEndpointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.env = patch.dict(os.environ, {"APP_MESSAGE": "Test message", "APP_VERSION": "test"})
        cls.env.start()
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), RequestHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.port = cls.server.server_address[1]

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)
        cls.env.stop()

    def get_json(self, path: str) -> tuple[int, dict]:
        connection = HTTPConnection("127.0.0.1", self.port, timeout=3)
        connection.request("GET", path)
        response = connection.getresponse()
        payload = json.loads(response.read())
        status = response.status
        connection.close()
        return status, payload

    def test_health_endpoint(self) -> None:
        status, payload = self.get_json("/healthz")
        self.assertEqual(status, 200)
        self.assertEqual(payload, {"status": "ok"})

    def test_info_uses_environment_configuration(self) -> None:
        status, payload = self.get_json("/api/info")
        self.assertEqual(status, 200)
        self.assertEqual(payload["message"], "Test message")
        self.assertEqual(payload["version"], "test")

    def test_unknown_path_returns_404(self) -> None:
        status, payload = self.get_json("/missing")
        self.assertEqual(status, 404)
        self.assertEqual(payload["error"], "not_found")


if __name__ == "__main__":
    unittest.main()
