# Week 13 Lab: Threat-model and harden your capstone

[← Practical labs](README.md) · [← Week 13 guide](../weeks/week-13.md) · [Starter API](starter-app/README.md)

## Mission
Review the capstone as an attacker would, identify risks, apply practical controls and record before/after evidence. Use only your own local project or an explicitly authorized training environment.

**Time:** 60–90 minutes · **Cost:** Free; Docker recommended

## Part A — Draw the trust boundaries
Sketch the path from user to application, workload identity, data store and external services. Mark:
- Public entry points and internal-only services
- Identities and permissions at each boundary
- Secrets and sensitive data flows
- Storage locations and who can read/write them
- Logs and the data they might expose

For each boundary, ask: what if this component is compromised?

## Part B — Threat-model one important flow
Use this lightweight STRIDE prompt:
| Threat category | Question to ask |
|---|---|
| Spoofing | Can someone impersonate a user or workload? |
| Tampering | Can an untrusted party change data or requests? |
| Repudiation | Can an important action happen without an audit trail? |
| Information disclosure | Can a user read secrets or another user's data? |
| Denial of service | Can one caller exhaust a resource? |
| Elevation of privilege | Can a low-privilege identity gain broader access? |

Choose at least three plausible threats. Record asset, threat, likelihood, impact, existing control and next action. This is a learning aid, not an exhaustive formal threat model.

## Part C — Inspect the container's security posture
From the repository root:
~~~bash
docker build -t cloud-track-demo:week-13 curriculum/labs/starter-app
docker image inspect cloud-track-demo:week-13 \
  --format 'User={{.Config.User}} ExposedPorts={{json .Config.ExposedPorts}}'
~~~

Expected: the configured user is a non-root account (`appuser`) and the image declares port 8080. If metadata differs, inspect the Dockerfile and explain the discrepancy.

Run the service with a tighter local runtime profile:
~~~bash
docker run -d --name cloud-track-secure \
  --read-only \
  --cap-drop=ALL \
  --security-opt=no-new-privileges \
  --pids-limit=64 \
  --memory=128m --cpus=0.5 \
  -p 127.0.0.1:18080:8080 \
  cloud-track-demo:week-13
curl -i http://127.0.0.1:18080/healthz
docker logs cloud-track-secure
~~~

Expected: HTTP 200. The service should run without writing to its container filesystem. These flags are a learning baseline, not a substitute for reviewing the runtime platform's controls.

## Part D — Review secrets and access
- Check that `.env`, private keys, service-account files and Terraform state are not tracked: `git status --short` and `git ls-files`.
- Inspect IAM bindings or local role definitions for broad permissions. Ask whether each identity needs every permission.
- Confirm secrets are injected through an approved secret store or runtime mechanism, not hard-coded into source or image layers.
- Confirm public access is intentional and unauthenticated endpoints return only safe-to-disclose data.

Optional secret scan: use the official [Gitleaks installation instructions](https://github.com/gitleaks/gitleaks). Scan the working tree with `gitleaks dir --redact --no-banner .`. Review findings; never paste detected secret values into a report. A clean scan does not prove secrets were never exposed in repository history or elsewhere.

## Core challenge
Fix at least one real finding in your own capstone or document why it is accepted for the demo. Examples: remove a tracked secret and rotate it, narrow an over-broad permission, bind a demo service to localhost, or remove sensitive fields from logs.

Record the risk, change, verification test and residual risk. If a real credential leak is found, stop using it and rotate/revoke it; deleting the line from the latest commit is not enough.

## Intermediate stretch
Add an automated secret or dependency check to CI. Explain false positives, false negatives, permissions and why a scan cannot replace human review.

## Troubleshooting
- If port 18080 is occupied, choose another unused local port and update the curl URL.
- If the read-only container fails, inspect logs and determine whether the app genuinely needs write access; do not remove restrictions without understanding why.
- Never test a third-party system without explicit authorization.
- Use synthetic data and redact identifiers in evidence.

## Cleanup
~~~bash
docker rm -f cloud-track-secure
~~~

Remove only the container created for this lab. Do not run broad Docker prune commands.

## Evidence
Submit `week-13-security-review.md` with a trust-boundary diagram, three prioritized threats, container posture output, one finding/remediation/verification, residual risk and cleanup confirmation.

Never submit secrets, private keys, personal data or unredacted logs.
