[← Back to Cloud Track home](../README.md)


# 🔐 Cloud Security Checklist

Use before demo day, and before making anything public.

## Identity and access
- [ ] No one has more access than they need (least privilege)
- [ ] No unused users or roles
- [ ] Apps use service accounts with narrow roles
- [ ] Two-factor authentication on every account
- [ ] No long-lived service account keys downloaded or stored in repos

## Secrets
- [ ] No passwords, tokens or keys in code, commits or screenshots
- [ ] `.env` and credential files are in `.gitignore`
- [ ] Secrets stored in a secret manager or repository secrets
- [ ] Any leaked secret has been revoked and replaced

## Data and storage
- [ ] Buckets are private unless they must be public
- [ ] Sensitive data is not stored when it is not needed
- [ ] Backups or recovery plan considered

## Network
- [ ] Only needed ports are open
- [ ] Public services are public on purpose
- [ ] Demo services are deleted after use

## Code and dependencies
- [ ] Dependencies are up to date
- [ ] Dependabot or similar alerts enabled
- [ ] CI runs tests on pull requests

## Logging and monitoring
- [ ] Audit logs available
- [ ] At least one alert configured
- [ ] You know where to look when something breaks

## Cost
- [ ] Budget alert set
- [ ] Unused resources deleted

## Terraform and infrastructure code
- [ ] State files and `*.tfvars` are not in Git
- [ ] Plans reviewed before applying

If you find something serious in someone else's project, tell them privately and kindly. See the [security policy](https://github.com/GDG-TUM/.github/blob/main/SECURITY.md).
