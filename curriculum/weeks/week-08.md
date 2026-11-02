# Week 08: Cloud compute and first deployment

[← All weekly guides](README.md) · [← Curriculum overview](../README.md) · [Step-by-step lab](../labs/week-08-cloud-run-deployment.md)

## Goal
Understand the Cloud Run deployment lifecycle and practise deploying only when an approved project, budget owner and cleanup plan are provided.

## Learning outcomes
Explain the concepts below, complete the core lab and identify one relevant failure mode, limitation or security/cost consideration.

## Concepts
Compute options; Cloud Run; container registry; revisions; environment config; scaling; startup; logs.

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
If the Track Lead has approved a shared project and all pre-deployment checks pass, deploy the Week 6 container to Cloud Run, verify its health endpoint and logs, then remove the service. Otherwise, complete the local Docker alternative in the [Week 8 lab](../labs/week-08-cloud-run-deployment.md); it is valid core evidence.

## Stretch challenge
Compare Cloud Run with a VM; explain scaling-to-zero, statelessness and persistent disk needs.

## Evidence to submit
Deployed endpoint or local equivalent, deployment notes and cleanup record.

Add evidence to your own learning log or capstone repository. Redact identifiers and sensitive values. A short explanation is more useful than an unexplained screenshot.

## Safety and cleanup
Cloud Run may incur charges. Verify pricing, quotas and billing eligibility.

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
