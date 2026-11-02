# Cloud Track Demo API

A deliberately small Python HTTP service used in Weeks 5–8. It uses only the Python standard library, so the local lab does not need a package installation or paid service.

## Run locally

Requires Python 3.10 or newer.

```bash
python3 --version
python3 app.py
```

In another terminal:

```bash
curl -i http://localhost:8080/
curl -i http://localhost:8080/healthz
curl -i http://localhost:8080/api/info
```

The service binds to `0.0.0.0` and uses `PORT` (default `8080`), as expected by Cloud Run. For local development, the default port is also 8080.

## Configure without changing code

```bash
APP_MESSAGE="Hello from my laptop" APP_VERSION="0.2.0" python3 app.py
```

Then request `/api/info`. These are demonstration settings, not secrets. Never put passwords, tokens or private keys in environment variables committed to a repository.

## Run tests

From this directory:

```bash
python3 -m unittest discover -s tests -v
```

The tests start a local server on an ephemeral loopback port and check the health, info and unknown-route responses.

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/` | Service overview |
| GET | `/healthz` | Lightweight health response |
| GET | `/api/info` | Non-sensitive runtime configuration |

Unknown paths return JSON with HTTP 404. Request logs are written to standard output.

This is a teaching starter, not a production API. It has no authentication, persistence, rate limiting or business-data handling. Do not expose sensitive data through it.
