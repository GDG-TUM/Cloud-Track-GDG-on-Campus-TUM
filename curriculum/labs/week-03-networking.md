# Week 3 Lab: Networking foundations

[← Practical labs](README.md) · [← Week 3 guide](../weeks/week-03.md)

## Mission
Trace a web request from a client to a server and use basic tools to investigate DNS, connectivity, ports and HTTP responses.

**Time:** 60–90 minutes · **Cost:** Free · **Target:** public documentation website

## Safety and scope
Use only public websites intended for general access, such as `example.com`. Do not scan networks, enumerate ports, brute-force services or test systems without explicit authorization. These exercises make ordinary DNS and HTTP requests only.

## Part A — Identify your network tools

```bash
command -v ping
command -v curl
command -v getent || command -v nslookup
command -v ip || command -v ifconfig
```

If a tool is missing, note it. Do not install random binaries from untrusted sites.

## Part B — Understand DNS

On Linux with glibc:

```bash
getent ahosts example.com
```

Alternative:

```bash
nslookup example.com
```

Expected: one or more IP addresses associated with the domain. Results can vary due to DNS, geography, caching and IPv4/IPv6.

**Explain:** DNS resolves a human-readable name to network records. It does not itself guarantee that a web server is healthy.

## Part C — Inspect an HTTP response

```bash
curl -I https://example.com
```

Expected: response headers, including an HTTP status line. A successful request commonly returns a 2xx or 3xx status. The exact status and headers may change.

Inspect a verbose connection:

```bash
curl -v --max-time 15 https://example.com -o /dev/null
```

Look for:
- DNS resolution
- Connection establishment
- TLS negotiation
- HTTP request and response status

Do not share verbose output without checking it for private proxy or network details.

## Part D — Distinguish ports and protocols

Read these common examples:

| Protocol | Typical port | Purpose |
|---|---:|---|
| HTTP | TCP 80 | Unencrypted web traffic |
| HTTPS | TCP 443 | HTTP protected by TLS |
| SSH | TCP 22 | Encrypted remote shell |
| DNS | 53 UDP and TCP | Name resolution |

A port identifies an application endpoint on a host. TCP and UDP are transport protocols with different delivery semantics.

## Part E — Check basic reachability

```bash
ping -c 4 example.com
```

Expected: either replies or a timeout/unreachable message. Some networks block ICMP, so ping failure does not prove a website is down.

Check the HTTPS application path instead:

```bash
curl -sS -o /dev/null -w 'HTTP %{http_code}\nDNS %{time_namelookup}s\nConnect %{time_connect}s\nTLS %{time_appconnect}s\nTotal %{time_total}s\n' --max-time 15 https://example.com
```

Expected: timing measurements and an HTTP status code. Timing varies.

## Part F — Draw the request journey

Create a diagram with these stages:

1. User enters `https://example.com`.
2. Browser resolves the hostname through DNS.
3. Client establishes a TCP connection to the destination on port 443.
4. TLS handshake establishes an encrypted channel.
5. Client sends an HTTP request.
6. Server returns an HTTP response.
7. Browser processes the response.

For each stage, name one possible failure. Examples: DNS failure, routing issue, blocked port, certificate problem, server error.

## Core challenge — Diagnose a failure

For each symptom, write the next safe diagnostic step:

| Symptom | Your next step |
|---|---|
| Domain does not resolve | |
| DNS works but TCP connection times out | |
| TLS certificate validation fails | |
| Server returns HTTP 404 | |
| Server returns HTTP 500 | |
| Ping fails but curl succeeds | |

Do not disable TLS verification as a fix. A 404 means the server was reached but the requested resource was not found; a 500 indicates a server-side error.

## Intermediate stretch
Compare `curl -I`, `curl -v` and the timing format above. Explain which layer each helps investigate. If `traceroute` or `tracepath` is already available, run it only against `example.com` and explain why intermediate routers may not respond.

## Troubleshooting
- **DNS command returns nothing:** try the alternate resolver command and check whether the network is connected.
- **Ping times out:** ICMP may be filtered; test the application with curl.
- **Curl reports certificate errors:** check system time and trust-store configuration; do not use `-k` to hide the problem.
- **Curl times out:** retry once, record the time and network, and compare with another approved network if available.
- **Proxy output appears:** redact proxy addresses and credentials before sharing logs.

## Evidence
Submit `week-03-evidence.md` with:
- DNS output (redacted if needed).
- HTTP status and timing output.
- Request-journey diagram.
- Answers to the six diagnostic scenarios.
- One failure you encountered and how you narrowed it down.

## Cleanup
No persistent resources are created. Remove any temporary output files containing network details before sharing your work.
