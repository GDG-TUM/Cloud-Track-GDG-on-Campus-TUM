[← Back to Cloud Track home](README.md)


# 🚀 Getting Started

Do this checklist once, ideally before Week 1. It takes about 45 minutes.

## 1. Accounts
- [ ] **GitHub account** with [two-factor authentication](https://docs.github.com/authentication/securing-your-account-with-two-factor-authentication-2fa) turned on
- [ ] Accepted your invitation to the **GDG-TUM** organization
- [ ] **Google account** you will use for cloud learning (a personal one is fine)
- [ ] **Google Cloud account** (done together in Week 1; check current free-tier and trial terms on the official site first)

> ⚠️ Cloud services can cost money if left running. Always set a **budget alert** (Week 1) and **delete resources** when an exercise ends.

## 2. Tools to install
| Tool | Why | Check it works |
|------|-----|----------------|
| **Git** | Version control | `git --version` |
| **A code editor** (VS Code recommended) | Writing code and configs | Opens a folder |
| **Docker Desktop** (or Docker Engine on Linux) | Containers | `docker --version` |
| **Google Cloud CLI** (`gcloud`) | Control Google Cloud from the terminal | `gcloud --version` |
| **Terraform** (needed by Week 8) | Infrastructure as Code | `terraform -version` |

If a tool won't install on your laptop (low RAM, old OS), tell the Track Lead. **Cloud Shell** in the Google Cloud console gives you a free browser terminal with most of these preinstalled.

## 3. Configure Git
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## 4. Join the community
- [ ] Join the track channel (link shared by the core team)
- [ ] Open a **Member Roadmap** issue in the `member-roadmaps` repo
- [ ] Make your first contribution: [add your profile](members/README.md)

## 5. Know the rules
- [Code of Conduct](https://github.com/GDG-TUM/.github/blob/main/CODE_OF_CONDUCT.md)
- [Contributing guide](https://github.com/GDG-TUM/.github/blob/main/CONTRIBUTING.md)
- [Security policy](https://github.com/GDG-TUM/.github/blob/main/SECURITY.md)
- Never commit passwords, API keys, tokens or `.env` files.

## ✅ Ready?
Go to [Week 1: Cloud fundamentals](weekly-sessions/week-01-cloud-fundamentals/README.md).
