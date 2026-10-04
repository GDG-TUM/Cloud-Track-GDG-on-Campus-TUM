[← Back to Cloud Track home](../../README.md)


# Week 8: Infrastructure as Code

**Date:** 30 Nov (draft; confirm time and venue in the track channel)

**Goal:** Define cloud resources in code.

## Learning objectives
By the end you should be able to:
- Explain providers, resources and state
- Run `init`, `plan`, `apply` and `destroy`
- Keep state and credentials out of Git

## Before the session
- [ ] Terraform installed
- [ ] Read [Stage 4](../../learning-path/04-cicd-and-iac.md)

## Agenda
1. Why IaC? (15 min)
2. Terraform walkthrough (25 min)
3. Hands-on: create and destroy a bucket (40 min)
4. State, secrets and good habits (10 min)

## Hands-on reference
```hcl
terraform {
  required_providers {
    google = { source = "hashicorp/google" }
  }
}

provider "google" {
  project = "YOUR_PROJECT_ID"
  region  = "REGION"
}

resource "google_storage_bucket" "demo" {
  name     = "YOUR-UNIQUE-BUCKET-NAME"
  location = "REGION"
}
```
```bash
terraform init
terraform plan
terraform apply
terraform destroy   # always clean up
```
Add `*.tfstate`, `.terraform/` and `*.tfvars` to `.gitignore`.

## 🏁 Take-home challenge
- [ ] Write Terraform for one resource in your capstone
- [ ] Run plan, apply and destroy
- [ ] Explain in two sentences why state files must not be public

Post your result or questions in the track channel, or open an issue.

## 📝 Session notes
Add slides, links, recordings and key takeaways here after the session (via pull request).

- Slides: _to be added_
- Recording: _to be added_
- Extra resources: _to be added_

---
[← Week 7](../week-07-cicd-github-actions/README.md) | [All sessions](../README.md) | [Week 9 →](../week-09-security-and-monitoring/README.md)
