[← Back to Cloud Track home](../../README.md)


# Week 7: CI/CD with GitHub Actions

**Date:** 23 Nov (draft; confirm time and venue in the track channel)

**Goal:** Automate build, test and deploy.

## Learning objectives
By the end you should be able to:
- Read and write a basic workflow
- Run tests on every pull request
- Use repository secrets safely
- Understand why short-lived credentials beat long-lived keys

## Before the session
- [ ] A repo with a small app and a test
- [ ] Read [Stage 4](../../learning-path/04-cicd-and-iac.md)

## Agenda
1. CI/CD concepts (15 min)
2. Workflow anatomy (20 min)
3. Hands-on: your first pipeline (45 min)
4. Secrets and authentication (10 min)

## Hands-on reference
Minimal workflow, saved as `.github/workflows/ci.yml` in **your project repo**:
```yaml
name: CI
on:
  pull_request:
  push:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: echo "replace with your test command"
```
For deploying to Google Cloud from Actions, prefer **Workload Identity Federation** over downloading service-account keys.

## 🏁 Take-home challenge
- [ ] Add a CI workflow to your capstone repo
- [ ] Make a pull request that fails the check, then fix it
- [ ] Never paste keys into workflow files; use repository secrets

Post your result or questions in the track channel, or open an issue.

## 📝 Session notes
Add slides, links, recordings and key takeaways here after the session (via pull request).

- Slides: _to be added_
- Recording: _to be added_
- Extra resources: _to be added_

---
[← Week 6](../week-06-debrief-and-data/README.md) | [All sessions](../README.md) | [Week 8 →](../week-08-infrastructure-as-code/README.md)
