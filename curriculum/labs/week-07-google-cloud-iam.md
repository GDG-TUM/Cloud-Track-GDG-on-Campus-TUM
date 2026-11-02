# Week 7 Lab: Google Cloud foundations and IAM

[← Practical labs](README.md) · [← Week 7 guide](../weeks/week-07.md)

## Mission
Understand the Google Cloud resource hierarchy, configure the CLI, inspect project and API state, and read IAM bindings without granting broad permissions.

**Time:** 60–90 minutes · **Cost:** Inspection only; a Google Cloud project may be needed for the optional CLI path.

## Important safety gate
You can complete Parts A–B without a cloud account. Do not create a billing account, attach payment details, enable APIs or change IAM policies unless the Track Lead has confirmed the project, budget, permissions and cleanup owner.

A budget alert is not a spending cap. Use a dedicated learning project, not a personal production project.

## Part A — Understand the hierarchy

Draw and label:

```text
Organization
└── Folder(s)
    └── Project
        └── Resources (for example: Cloud Run service, Artifact Registry repository)
```

Not every learner has an organization or folder. A project can exist directly under an organization or be standalone.

Explain:
- Why project boundaries help organize resources and permissions.
- Why project ID, project name and project number are different concepts.
- Why IAM roles should be scoped as narrowly as practical.

## Part B — Check the CLI

```bash
gcloud version
gcloud auth list
gcloud config list
gcloud projects list
```

Expected: CLI version, active authenticated account (if any), current configuration and projects visible to that account. An empty project list or permission error does not mean the CLI is broken.

If you do not have an approved project, stop here and use the hierarchy sketch and role-reading exercises.

## Part C — Select the approved project

Only after the facilitator supplies/approves a dedicated project ID:

```bash
gcloud config set project PROJECT_ID
gcloud config get-value project
gcloud projects describe PROJECT_ID
```

Replace `PROJECT_ID` with the exact approved ID. Verify it before any command that changes resources. Never paste a project identifier into public evidence if your organization considers it sensitive.

## Part D — Inspect APIs without enabling them

```bash
gcloud services list --enabled --project=PROJECT_ID
```

This is read-only. For Week 8, the deployment workflow may require Cloud Run, Cloud Build and Artifact Registry APIs. Do not enable them in this lab unless the project owner has approved the deployment exercise.

## Part E — Read IAM policy

```bash
gcloud projects get-iam-policy PROJECT_ID \
  --format='table(bindings.role,bindings.members)'
```

This is a read-only inspection. Output may contain email addresses and service identities; redact them before sharing.

Understand:
- **Principal:** the user, group or service identity receiving access.
- **Role:** a collection of permissions.
- **Policy binding:** connects a principal to a role at a resource scope.
- **Inheritance:** permissions can be inherited from parent resources.

Do not run `gcloud projects add-iam-policy-binding` or grant `roles/owner` for this exercise.

## Part F — Human identity vs workload identity

A human uses an interactive identity to operate the CLI and console. An application running on Cloud Run should use a dedicated service identity with only the permissions it needs. Do not download service-account JSON keys or commit credentials.

Write one example of a task that a human operator needs to perform and one API action that an application might need. Explain why they should not automatically share the same permissions.

## Core challenge
Read the official Cloud Run deployment permissions documentation linked from the resource section. List the capabilities needed by:
- A person deploying a service.
- The Cloud Run service identity at runtime.

Explain why deployer permissions and runtime permissions are separate concerns.

## Intermediate stretch
Using a facilitator-provided sandbox only, inspect a service account's roles and propose a least-privilege alternative to a broad project-level role. Do not apply the change. Ask the owner to review it.

## Troubleshooting
- **No active account:** authenticate only with your own approved account using the organization's documented process.
- **No projects listed:** ask the owner to verify project membership; do not create a new billing project to work around access.
- **Permission denied:** record the command and error after redacting identifiers. Ask for the narrow permission needed; do not request Owner by default.
- **API not enabled:** do not enable it until the owner approves the Week 8 deployment and associated costs.

## Evidence
Submit `week-07-evidence.md` with hierarchy diagram, CLI version, redacted read-only inspection notes, explanation of principals/roles/bindings, and a least-privilege proposal.

## Cleanup
No resource creation is required. If the facilitator granted temporary access, ask them to remove it when the lab period ends.
