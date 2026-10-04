[← Back to Cloud Track home](../README.md)


# Stage 4: CI/CD and Infrastructure as Code

**Goal:** Stop doing things by hand. Automate builds, tests, deploys and infrastructure.

**Matching session:** [week-07-cicd-github-actions](../weekly-sessions/week-07-cicd-github-actions/README.md)

## What you will learn
- Continuous Integration: build and test on every push
- Continuous Delivery/Deployment: ship automatically
- GitHub Actions: workflows, jobs, steps, secrets
- Infrastructure as Code with Terraform: providers, resources, plan, apply, destroy, state
- Why long-lived keys are risky and what safer authentication looks like

## Hands-on
1. Add a GitHub Actions workflow that runs tests on every pull request.
2. Write a Terraform file that creates one resource, apply it, then destroy it.
3. Keep the Terraform state file and any credentials **out of Git**.

## Free resources
See [resources](../resources/free-resources.md) for official docs, labs and tutorials.

## ✅ Checkpoint
- Can I read a workflow YAML file and explain when it runs?
- What do `terraform plan` and `terraform apply` each do?
- Where do secrets belong, and where must they never go?

If you can answer these, move to the next stage. If not, revisit the topics or ask in the track channel.

[← Learning path overview](README.md)
