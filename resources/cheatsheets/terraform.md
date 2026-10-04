[← Back to Cloud Track home](../../README.md)

# Terraform Cheat Sheet

```bash
terraform init       # download providers, set up the folder
terraform fmt        # tidy formatting
terraform validate   # check syntax
terraform plan       # preview changes
terraform apply      # make the changes
terraform destroy    # remove everything it created
terraform state list # what it manages
```
**Never commit:** `*.tfstate`, `*.tfstate.backup`, `.terraform/`, `*.tfvars` with secrets.

[← All resources](../README.md)
