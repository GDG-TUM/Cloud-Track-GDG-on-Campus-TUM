# Week 12: Infrastructure as Code with Terraform

[← All weekly guides](README.md) · [← Curriculum overview](../README.md) · [Step-by-step lab](../labs/week-12-terraform-iac.md)

## Goal
Describe and safely manage infrastructure changes declaratively.

## Learning outcomes
Explain the concepts below, complete the core lab and identify one relevant failure mode, limitation or security/cost consideration.

## Concepts
Providers; resources; variables; outputs; init/validate/fmt/plan/apply/destroy; state; drift; modules.

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
Use a local provider or tightly scoped cloud example. Run fmt, validate and plan; inspect changes before applying; destroy temporary resources.

## Stretch challenge
Refactor repeated configuration into a module and explain state security and locking.

## Evidence to submit
Terraform configuration, sanitized plan output and lifecycle instructions.

Add evidence to your own learning log or capstone repository. Redact identifiers and sensitive values. A short explanation is more useful than an unexplained screenshot.

## Safety and cleanup
Never commit state files, credentials or sensitive tfvars. Review every plan.

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
