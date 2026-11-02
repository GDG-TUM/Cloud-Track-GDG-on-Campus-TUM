[← Back to Cloud Track home](README.md)

# Getting Started

Complete this checklist before Week 1. You do not need a paid cloud account to begin the first four weeks.

## 1. Accounts
- [ ] GitHub account with [two-factor authentication](https://docs.github.com/authentication/securing-your-account-with-two-factor-authentication-2fa) enabled
- [ ] Accepted your invitation to the GDG-TUM organization, if applicable
- [ ] Google account for later Google Cloud activities; do not enable billing unless the facilitator has explained the cost and approval process

**Cost and safety:** Cloud resources can incur charges. A budget notification is not a spending cap. Do not enter payment details or enable billing just to complete Weeks 1–4. Never share credentials or commit tokens, private keys, service-account files or `.env` files.

## 2. Tools to install

| Tool | First used | Check |
|---|---:|---|
| Bash-compatible terminal (Linux, macOS or WSL) | Week 2 | `echo "$SHELL"` |
| Git | Week 4 | `git --version` |
| Code editor | Week 4 onward | Open a folder |
| curl and DNS lookup utility | Week 3 | `curl --version`, `command -v getent` |

Docker, Google Cloud CLI and Terraform are introduced later. Do not install everything in advance if your device has limited storage or connectivity.

If a tool cannot be installed, tell the Track Lead. Ask about a lab machine or another approved alternative; Cloud Shell may be useful for selected later activities but is not required for Weeks 1–4.

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
3. Complete the [practical labs](curriculum/labs/README.md) for Weeks 1–4.
4. Keep your evidence in a learning log or personal repository. Redact private information.

You are ready to begin with [Week 1: Cloud concepts and safe setup](curriculum/labs/week-01-cloud-concepts.md).
