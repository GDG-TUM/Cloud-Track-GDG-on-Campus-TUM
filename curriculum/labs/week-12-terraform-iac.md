# Week 12 Lab: Manage a local resource with Terraform

[← Practical labs](README.md) · [← Week 12 guide](../weeks/week-12.md)

## Mission
Describe infrastructure declaratively, inspect a plan, apply a small change and destroy it. Use Terraform's local provider to create a text file. No paid cloud resources.

**Time:** 60–90 minutes · **Cost:** Free; provider download requires internet

## Part A — Install Terraform
Use the official [HashiCorp installation instructions](https://developer.hashicorp.com/terraform/install).
```bash
terraform version
mkdir -p ~/cloud-track-week-12
cd ~/cloud-track-week-12
```

Do not run Terraform with elevated privileges.

## Part B — Write configuration
Create `main.tf`:
```hcl
terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

variable "student_label" {
  description = "A non-sensitive label for this local lab"
  type        = string
  default     = "cloud-track-learner"
}

resource "local_file" "lab_note" {
  filename = "terraform-managed-note.txt"
  content  = var.student_label
}

output "created_file" {
  description = "Path to the local file managed by this configuration"
  value       = local_file.lab_note.filename
}
```

Create `.gitignore`:
```gitignore
.terraform/
*.tfstate
*.tfstate.*
*.tfvars
crash.log
terraform-managed-note.txt
```

State can contain sensitive values. Never commit state files, local variable files or credentials.

## Part C — Format, initialize and validate
```bash
terraform fmt -check
terraform init
terraform validate
```

If formatting differs, run `terraform fmt` and repeat the check.

## Part D — Inspect and apply
```bash
terraform plan
terraform apply
cat terraform-managed-note.txt
terraform show
terraform output
```

Read the plan. Type `yes` only after confirming it proposes the expected single local file.

## Part E — Change configuration
Change the default `student_label` and run `terraform plan`. Explain why Terraform proposes an update. Apply and inspect the file again.

## Core challenge
Add a second `local_file` resource and output. Run fmt, validate and plan before applying.

## Intermediate stretch
Pass a variable with `-var='student_label=week-12-practice'`. Explain provider, resource, variable, output and state. Research remote state, locking, drift and modules without configuring a shared backend.

## Cloud extension — approval required
A facilitator may demonstrate a cloud provider in an approved sandbox. Verify project, identity, region, resource types, quotas, pricing and cleanup owner before apply. Review the complete plan with the project owner. This local lab is valid and requires no billing.

## Troubleshooting
Retry provider download if network access is interrupted; do not download binaries from untrusted sites. Ensure no other Terraform process is using the directory if state is locked. Read why Terraform proposes replacement before applying. Never commit state or generated artifacts.

## Cleanup
```bash
terraform destroy
test ! -e terraform-managed-note.txt && echo "Lab file removed"
```

Review the destroy plan and confirm. Keep only sanitized evidence; remove the lab directory when finished.

## Evidence
Submit `week-12-evidence.md` with configuration, sanitized plan summary, lifecycle explanation, state-file safety and destroy confirmation. Never submit `.tfstate` or credentials.
