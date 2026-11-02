# Week 11 Lab: Automate tests with GitHub Actions

[← Practical labs](README.md) · [← Week 11 guide](../weeks/week-11.md) · [Starter app](starter-app/README.md)

## Mission
Create CI that tests the shared API and verifies its Docker image builds. A pull request receives a visible pass/fail result before merge.

**Time:** 60–90 minutes · **Cost:** GitHub account; no cloud account

## Part A — Run checks locally
From the repository root:
```bash
cd curriculum/labs/starter-app
python3 -m unittest discover -s tests -v
docker build -t cloud-track-demo:week-11 .
```

Fix or report local failures before automating them.

## Part B — Add or inspect a workflow
In your **own capstone repository**, create `.github/workflows/cloud-track-ci.yml` with the example below. If you are practising inside this Cloud Track curriculum repository, that file already exists: inspect it rather than trying to create a duplicate. The existing workflow is intentionally scoped to changes in the shared starter app and this workflow file.
```yaml
name: Cloud Track CI

on:
  pull_request:
    paths:
      - "curriculum/labs/starter-app/**"
      - ".github/workflows/cloud-track-ci.yml"
  push:
    branches: ["main"]
    paths:
      - "curriculum/labs/starter-app/**"
      - ".github/workflows/cloud-track-ci.yml"

permissions:
  contents: read

jobs:
  test-and-build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Run unit tests
        working-directory: curriculum/labs/starter-app
        run: python -m unittest discover -s tests -v
      - name: Build Docker image
        run: docker build -t cloud-track-demo:ci curriculum/labs/starter-app
```

This workflow is read-only and does not publish an image or deploy infrastructure. Review action versions and repository policy before cohort use. In your own project, adjust the `paths` filters and working directory to match your app and tests.

## Part C — Open a pull request
```bash
git switch -c lab/week-11-ci
git add .github/workflows/cloud-track-ci.yml
git commit -m "ci: add Cloud Track test and image build workflow"
git push -u origin lab/week-11-ci
```

Open a PR against main. Inspect the Checks section and individual steps.

## Part D — Prove failures are visible
In a temporary branch only, change one expected test value to an intentionally incorrect value. Push and confirm CI fails, then revert immediately. Never merge a deliberately failing test or weaken tests to get a green result.

## Core challenge
Explain the trigger, runner, test step, failure behaviour and why deployment credentials are not required.

## Intermediate stretch
Add a Python-version matrix after checking compatibility. Explain least-privilege permissions, why untrusted PR code must not receive deployment secrets, and how protected environments or short-lived identity federation could be used later.

## Troubleshooting
Check YAML indentation, branch names, path filters and the Actions tab if no run appears. Reproduce Docker build failures locally. Compare Python versions, working directory and environment if tests differ between local and CI.

## Cleanup and evidence
Close or merge the learning PR as instructed and delete temporary branches. No cloud resources are created. Submit the workflow, successful run URL, evidence of the deliberate failure and a permissions explanation.
