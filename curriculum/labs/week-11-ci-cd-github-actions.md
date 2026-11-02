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
This Cloud Track repository already contains `.github/workflows/cloud-track-ci.yml`. When completing the lab here, inspect that existing workflow and map each section to the concepts below; do not try to create a duplicate. To practise authoring CI in your **own capstone repository**, create a workflow there using the example, then change the `paths`, working directory and build command to match files that actually exist in that repository.
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

This workflow is read-only and does not publish an image or deploy infrastructure. The example paths and working directory refer specifically to this curriculum repository's starter app; they will not work unchanged in a separate project unless you copy the app into the same directory structure. Review action versions and repository policy before cohort use.

## Part C — Trigger and inspect CI

**Working in this curriculum repository:** create a branch, make a small meaningful change under `curriculum/labs/starter-app/` (for example, add a test), run the checks locally, then push and open a PR. The existing path filter will trigger the workflow for that change.

**Working in your own capstone repository:** add your adapted workflow and the corresponding app/test changes to a feature branch, then push and open a PR.

```bash
git switch -c lab/week-11-ci
# Stage the workflow and/or the app/test files you changed.
git add .github/workflows/cloud-track-ci.yml curriculum/labs/starter-app/
git commit -m "ci: add or exercise the Cloud Track CI workflow"
git push -u origin lab/week-11-ci
```

If you are working in this curriculum repository, omit the workflow path from `git add` unless you actually changed it. Open a PR against `main`, then inspect the Checks section and individual steps.

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
