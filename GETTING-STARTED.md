[← Back to Cloud Track home](README.md)

# Getting Started

Complete the basics before Week 1. Install later tools when the relevant week approaches; you do not need every tool on day one.

## 1. Accounts
- [ ] GitHub account with [two-factor authentication](https://docs.github.com/authentication/securing-your-account-with-two-factor-authentication-2fa) enabled
- [ ] Accepted your invitation to the GDG-TUM organization, if applicable
- [ ] Google account for later Google Cloud activities; do not enable billing unless the facilitator has explained the cost and approval process

**Cost and safety:** Cloud resources can incur charges. A budget notification is not a spending cap. Do not enter payment details or enable billing just to complete the first seven weeks. Week 8 deployment is optional unless the Track Lead provides an approved project, permissions, budget owner and cleanup plan. Never share credentials or commit tokens, private keys, service-account files or `.env` files.

## 2. Tools to install gradually

| Tool | First used | Check |
|---|---:|---|
| Bash-compatible terminal (Linux, macOS or WSL) | Week 2 | `echo "$SHELL"` |
| curl and DNS lookup utility | Week 3 | `curl --version`, `command -v getent` |
| Git | Week 4 | `git --version` |
| Python 3.10+ | Week 5 | `python3 --version` |
| Docker Engine or Docker Desktop | Week 6 | `docker version` |
| Google Cloud CLI | Week 7 | `gcloud version` |

Terraform is introduced in Week 12. There is no need to install it yet. If a tool cannot be installed because of device, storage or connectivity limits, tell the Track Lead and ask about an approved alternative.

## 3. Configure Git before Week 4

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Use an email address you are comfortable associating with public commits. Check the values with `git config --global --list`.

## 4. Join the community
- [ ] Join the track channel (link shared by the core team)
- [ ] Open a Member Roadmap issue in the `member-roadmaps` repository, if requested
- [ ] Read the [GDG-TUM Code of Conduct](https://github.com/GDG-TUM/.github/blob/main/CODE_OF_CONDUCT.md)
- [ ] Read the [contributing guide](https://github.com/GDG-TUM/.github/blob/main/CONTRIBUTING.md)

## 5. Start learning
1. Read the [16-week curriculum](curriculum/README.md).
2. Open the [weekly session guides](curriculum/weeks/README.md).
3. Complete the [practical labs](curriculum/labs/README.md) in sequence.
4. Keep evidence in a learning log or personal repository. Redact private information.

Start with [Week 1: Cloud concepts and safe setup](curriculum/labs/week-01-cloud-concepts.md). Python, Docker and Google Cloud CLI become relevant later; cloud billing is not required for the local labs.
