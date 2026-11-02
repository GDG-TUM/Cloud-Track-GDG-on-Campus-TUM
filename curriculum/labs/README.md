# Practical Labs

[← Curriculum](../README.md) · [← Cloud Track home](../../README.md)

These labs turn the weekly curriculum into repeatable, evidence-led exercises. Complete the core path first. Stretch tasks are optional.

| Week | Lab | Main output | Cloud account required? |
|---:|---|---|---|
| 1 | [Cloud concepts and safe setup](week-01-cloud-concepts.md) | Architecture sketch and risk checklist | No |
| 2 | [Linux and CLI foundations](week-02-linux-cli.md) | Reproducible terminal task log | No |
| 3 | [Networking foundations](week-03-networking.md) | Request trace and diagnostic report | No |
| 4 | [Git collaboration](week-04-git-collaboration.md) | Reviewed pull request | GitHub account recommended |
| 5 | [Application runtime](week-05-application-runtime.md) | Tested Python HTTP API | No |
| 6 | [Docker workflows](week-06-docker-workflows.md) | Non-root container image and run evidence | No |
| 7 | [Google Cloud and IAM](week-07-google-cloud-iam.md) | Resource hierarchy and least-privilege review | Optional; read-only path available |
| 8 | [Cloud Run deployment](week-08-cloud-run-deployment.md) | Deployed service or local equivalent | Approved project and billing required for deployment |
| 9 | [Storage and databases](week-09-storage-databases.md) | SQLite persistence and storage decision | No |
| 10 | [Cloud networking](week-10-cloud-networking.md) | Container connectivity diagram and test | No; Docker required |
| 11 | [CI/CD with GitHub Actions](week-11-ci-cd-github-actions.md) | Automated test/build workflow | GitHub account |
| 12 | [Terraform and IaC](week-12-terraform-iac.md) | Terraform plan/apply/destroy evidence | No; local provider |

## Shared starter application

Weeks 5–8 use the [Cloud Track Demo API](starter-app/README.md). Members build it locally, containerize it, inspect Google Cloud IAM and deploy it (optional). Week 11 adds a CI workflow that tests and builds this same starter app.

## Lab conventions
- Commands are written for a Bash-compatible shell (Linux, macOS, or WSL) unless noted.
- Run commands one at a time and inspect output before continuing.
- Your output may differ by OS, network, package version or account. Learn to interpret it rather than copy a screenshot.
- Never paste secrets, access tokens, private keys, personal data or unredacted billing details into evidence.
- If a command is unavailable, record the OS and error, then use the alternative in troubleshooting.
- Keep a learning log with: objective, commands, result, explanation, issue encountered and cleanup.
- Cloud deployment is optional unless the Track Lead has provided an approved project, permissions, budget owner and cleanup plan. Local alternatives are valid evidence.

## Evidence standard
A lab is complete when another student can follow your notes and understand what you did, what happened, and what you learned. Screenshots alone are not sufficient; include commands and short explanations with sensitive values redacted.
