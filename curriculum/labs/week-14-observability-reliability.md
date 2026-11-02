# Week 14 Lab: Observe, diagnose and recover

[← Practical labs](README.md) · [← Week 14 guide](../weeks/week-14.md) · [Starter API](starter-app/README.md)

## Mission
Collect useful telemetry from the capstone, define service indicators and practise a small incident using a local container. Learn to distinguish evidence from assumptions.

**Time:** 60–90 minutes · **Cost:** Free; Docker and curl recommended

## Part A — Start the service
From the repository root:
~~~bash
docker build -t cloud-track-demo:week-14 curriculum/labs/starter-app
docker run -d --name cloud-track-observe \
  -p 127.0.0.1:18081:8080 cloud-track-demo:week-14
curl -i http://127.0.0.1:18081/healthz
curl -i http://127.0.0.1:18081/api/info
~~~

## Part B — Collect telemetry
Generate requests and inspect response codes and elapsed time:
~~~bash
for path in /healthz /api/info /missing; do
  curl -sS -o /dev/null \
    -w "$path status=%{http_code} time=%{time_total}s\n" \
    "http://127.0.0.1:18081$path"
done

docker logs --timestamps cloud-track-observe
docker stats --no-stream cloud-track-observe
~~~

Identify:
- **Logs:** event records that help explain what happened.
- **Metrics:** numeric measurements over time, such as request rate, error ratio, latency and resource use.
- **Traces:** a request's path across instrumented components. This single-service lab does not generate distributed traces.

Do not confuse one curl measurement with a statistically meaningful latency distribution.

## Part C — Define service indicators
Write two measurable indicators:
- Availability: successful eligible requests divided by total eligible requests.
- Latency: proportion of requests completed below a chosen threshold.

For a demo exercise, choose a target such as 95% of requests under 500 ms across a stated observation window. This is a teaching example, not a production recommendation. State how health checks, synthetic requests and real user traffic differ.

An SLO is a target for an indicator over a window. An alert should prompt an action; avoid alerting on every harmless event.

## Part D — Run a controlled incident
Stop the local container, verify the request fails, then restore it:
~~~bash
docker stop cloud-track-observe
curl --max-time 3 -i http://127.0.0.1:18081/healthz || echo "Request failed as expected"
docker start cloud-track-observe
curl -i http://127.0.0.1:18081/healthz
docker logs --since 5m cloud-track-observe
~~~

Create an incident note:
1. **Impact:** what could a user not do?
2. **Detection:** what signal showed the issue?
3. **Timeline:** when did you stop, detect and restore the service?
4. **Diagnosis:** what evidence supports the cause?
5. **Recovery:** what action restored service?
6. **Follow-up:** what would reduce detection or recovery time?

Do not claim that application logs identify the stop event; container lifecycle state and failed requests provide that evidence.

## Core challenge
Produce a one-page runbook for one likely failure: service unavailable, bad configuration, dependency unavailable or elevated error rate. Include symptom, checks, safe mitigation, escalation and recovery verification.

## Intermediate stretch
Create a small shell script that samples the health endpoint ten times and reports success count and elapsed times. Explain why this is a synthetic check and how you would avoid leaking credentials or high-cardinality personal data in telemetry.

## Cost and reliability discussion
Compare an always-on instance with scale-to-zero for a low-traffic student demo. Discuss cold starts, availability needs, quotas, log retention and alert noise. A budget alert is not a spending cap.

## Cleanup
~~~bash
docker rm -f cloud-track-observe
~~~

Remove only the container created for this lab.

## Evidence
Submit `week-14-operations-review.md` with telemetry samples, two indicators and their windows, incident timeline, runbook and cleanup confirmation. Redact identifiers and secrets.
