# Week 15 Lab: Prepare a release candidate

[← Practical labs](README.md) · [← Week 15 guide](../weeks/week-15.md)

## Mission
Turn the capstone into a reproducible release candidate. Another team should be able to understand it, run its checks, identify its security boundaries and explain how to recover from a failed release.

**Time:** 90–120 minutes · **Cost:** Free local workflow; cloud deployment must already be approved

## Part A — Freeze the release scope
Write a short release note containing:
- Problem and intended user.
- The one core user journey that must work.
- Included changes and explicitly deferred work.
- Known limitations and dependencies.
- Release owner and rollback/recovery contact for the demo.

Do not add features merely to make the project look more complex.

## Part B — Reproduce the build and tests
For the shared starter API, run from the repository root:
~~~bash
python3 -m unittest discover -s curriculum/labs/starter-app/tests -v
docker build -t cloud-track-demo:release-candidate curriculum/labs/starter-app
docker image inspect cloud-track-demo:release-candidate \
  --format 'User={{.Config.User}} Ports={{json .Config.ExposedPorts}}'
~~~

For your own capstone, document equivalent clean setup, test, build and run commands. Confirm GitHub Actions checks are green for the exact commit being considered. If a check has not run, mark it unverified rather than assuming it passed.

## Part C — Run the release checklist
- [ ] Core user journey works with synthetic/demo data.
- [ ] Setup, test, build and run instructions work from a clean checkout.
- [ ] Tests cover the critical path and at least one failure path.
- [ ] CI is green on the release commit; failed or skipped checks are explained.
- [ ] No credentials, private keys, `.env` files or Terraform state are tracked.
- [ ] IAM follows least privilege; public endpoints expose only intended data.
- [ ] Container runs as non-root and has a documented resource profile.
- [ ] Logs are useful and do not expose secrets or personal data.
- [ ] Health check and incident runbook are documented.
- [ ] Cloud resources, region, permissions, estimated cost and cleanup owner are documented if deployed.
- [ ] Architecture diagram matches the actual implementation.
- [ ] Known limitations and accepted risks are visible in the README.

## Part D — Peer review
Ask a different team to follow the README without verbal instructions. Ask them to identify prerequisites and architecture, run one test and the core workflow, find health/log/cleanup instructions, and explain one security boundary and one known limitation.

Record each blocker, severity, owner and disposition. Fix the highest-priority issue and repeat the affected check.

## Part E — Release and rollback plan
Create a short release plan:
- Version or commit SHA being demonstrated.
- Preconditions and verification steps.
- How to stop or roll back the demo.
- How to restore data, if relevant.
- Who can approve a production or cloud change.

For local Docker demos, retain the previous known-good image tag until the new version passes smoke tests. Do not delete or overwrite shared resources during practice.

## Core challenge
Produce a release-candidate README section with exact setup/test/run/cleanup commands and a clear statement of what has not been tested.

## Intermediate stretch
Add a meaningful reliability or security improvement, update CI and write a brief architecture decision record explaining the trade-off.

## Cleanup
Remove only temporary containers and resources created for the release rehearsal. Keep sanitized test evidence and release notes.

## Evidence
Submit release candidate commit/tag, completed checklist, peer review notes and remediation, release/rollback plan, updated README and known limitations.

A successful demo is not proof of production readiness. Be precise about what the team verified.
