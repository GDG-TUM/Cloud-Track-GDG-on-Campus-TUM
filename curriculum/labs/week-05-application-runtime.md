# Week 5 Lab: Build and inspect an HTTP application

[← Practical labs](README.md) · [← Week 5 guide](../weeks/week-05.md)

## Mission
Run a small HTTP API, inspect its routes and logs, configure it through environment variables, and test its behaviour.

**Time:** 60–90 minutes · **Cost:** Free · **Cloud account:** Not required

## Prerequisites
- Complete Weeks 2–4 or know basic terminal navigation and Git.
- Python 3.10+.
- curl (or a browser for basic requests).

## Part A — Get the starter application

From the repository root:

```bash
cd curriculum/labs/starter-app
python3 --version
```

Inspect `app.py` before running it. Find:
- The HTTP request handler.
- The three supported GET paths.
- Where `APP_MESSAGE`, `APP_VERSION` and `PORT` are read.
- Where request logs are written.

## Part B — Start the service

```bash
python3 app.py
```

Keep this terminal open. The server should report that it is listening on `0.0.0.0:8080`.

Open a second terminal in the same directory:

```bash
curl -i http://localhost:8080/
curl -i http://localhost:8080/healthz
curl -i http://localhost:8080/api/info
```

Expected:
- `/` returns HTTP 200 and a short service description.
- `/healthz` returns HTTP 200 with `{"status":"ok"}`.
- `/api/info` returns HTTP 200 and the current app message/version.

The server terminal should show a request log for each request.

## Part C — Inspect status codes

```bash
curl -i http://localhost:8080/does-not-exist
```

Expected: HTTP 404 and a JSON error response.

Explain the difference between:
- HTTP 200: request succeeded.
- HTTP 404: requested route was not found.
- HTTP 500: server encountered an unexpected error.

## Part D — Configure the running application

Stop the server with Ctrl+C. Restart with non-secret configuration:

```bash
APP_MESSAGE="Hello GDG TUM" APP_VERSION="0.2.0" python3 app.py
```

In the second terminal:

```bash
curl -sS http://localhost:8080/api/info
```

Expected: the response includes the new message and version without a source-code edit.

An environment variable is a configuration delivery mechanism, not automatically a secure secret store. Do not use this exercise to pass real credentials.

## Part E — Run automated tests

Stop the server. Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: three tests pass. The test suite starts its own temporary local HTTP server, so you do not need to run `app.py` at the same time.

## Core challenge
Add a new `GET /api/status` endpoint that returns:
- `service`: `cloud-track-demo`
- `status`: `available`
- `version`: the configured `APP_VERSION`

Add a test that verifies the endpoint returns HTTP 200 and the expected JSON fields. Re-run the complete test suite.

## Intermediate stretch
Add basic query-string handling to `/api/info` using Python's `urllib.parse`. Reject unsupported methods with a clear HTTP 405 response. Add tests for both cases. Do not echo arbitrary user input into HTML.

## Troubleshooting
- **Address already in use:** another process is listening on port 8080. Stop the process you started, or run with `PORT=8081 python3 app.py` and update the curl URL.
- **curl cannot connect:** confirm the server terminal is still running and the URL/port match.
- **Module import error in tests:** run tests from this directory, not the repository root.
- **Unexpected output:** inspect the response status and body with `curl -i`; inspect the server terminal for the corresponding request log.

## Evidence
Submit `week-05-evidence.md` with:
- Python version and start command.
- Output/status from all three endpoints plus the 404 test.
- One example of environment-based configuration.
- Test output.
- Explanation of why configuration and secrets are not the same.
- Your new endpoint and test (core challenge).

## Cleanup
Stop the server with Ctrl+C. No cloud resources are created.
