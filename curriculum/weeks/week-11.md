# Week 11: CI/CD with GitHub Actions

[← All weekly guides](README.md) · [← Curriculum overview](../README.md)

## Goal
Automate quality checks and build steps when code changes.

## Learning outcomes
Explain the concepts below, complete the core lab and identify one relevant failure mode, limitation or security/cost consideration.

## Concepts
Workflow YAML; events; jobs; runners; actions; environment variables; secrets; tests; build; deployment gates.

## Before the session
- Read this guide and bring questions.
- Ensure access to a terminal and GitHub.
- Check [Getting Started](../../GETTING-STARTED.md) and [Resources](../../resources/README.md).
- No paid service or cloud account is assumed unless the facilitator confirms access and alternatives.

## 90-minute session plan
| Time | Activity |
|---:|---|
| 0–10 min | Recap, goals and prerequisite check |
| 10–25 min | Concept walkthrough |
| 25–40 min | Instructor demonstration |
| 40–70 min | Guided core lab |
| 70–82 min | Checkpoint and stretch task |
| 82–90 min | Cleanup, reflection and next steps |

## Core lab
Create a workflow that runs tests and a build on pull requests. Confirm a failing test causes failure.

## Stretch challenge
Add dependency caching, matrix tests or protected deployment environment; explain workflow permissions.

## Evidence to submit
Passing CI run and explanation of each job.

Add evidence to your own learning log or capstone repository. Redact identifiers and sensitive values. A short explanation is more useful than an unexplained screenshot.

## Safety and cleanup
Use repository secrets only when required. Prefer short-lived identity federation over long-lived keys where supported.

## Checkpoint
- [ ] I can explain the main concepts in my own words.
- [ ] I completed the core lab or documented an equivalent alternative.
- [ ] I can show evidence and reproduce the result.
- [ ] I identified a limitation, failure mode or trade-off.
- [ ] I cleaned up temporary resources and checked for exposed secrets.

## Reflection
1. What was new or confusing?
2. What failed, and how did you investigate it?
3. What would you do differently next time?
