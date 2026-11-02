"""Small standard-library HTTP service used by the Cloud Track labs."""

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    server_version = "CloudTrackDemo/1.0"

    def _send_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/healthz":
            self._send_json(200, {"status": "ok"})
            return

        if self.path == "/api/info":
            self._send_json(
                200,
                {
                    "app": "cloud-track-demo",
                    "message": os.getenv("APP_MESSAGE", "Hello from the Cloud Track!"),
                    "version": os.getenv("APP_VERSION", "1.0.0"),
                },
            )
            return

        if self.path == "/":
            self._send_json(
                200,
                {
                    "service": "Cloud Track Demo API",
                    "endpoints": ["/healthz", "/api/info"],
                },
            )
            return

        self._send_json(404, {"error": "not_found", "path": self.path})

    def log_message(self, fmt: str, *args: object) -> None:
        # Keep request logs on stdout so Docker and Cloud Run can collect them.
        super().log_message(fmt, *args)


def main() -> None:
    port = int(os.getenv("PORT", "8080"))
    host = os.getenv("HOST", "0.0.0.0")
    server = ThreadingHTTPServer((host, port), RequestHandler)
    print(f"Starting Cloud Track Demo API on {host}:{port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Shutdown requested", flush=True)
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
