# Week 05: Application runtime and configuration

[← All weekly guides](README.md) · [← Curriculum overview](../README.md) · [Step-by-step lab](../labs/week-05-application-runtime.md)

## Goal
Explain how a web app starts, receives requests and reads configuration.

## Learning outcomes
Explain the concepts below, complete the core lab and identify one relevant failure mode, limitation or security/cost consideration.

## Concepts
Processes; ports; HTTP; entry point; environment variables; config vs secrets; health endpoints; logs; graceful shutdown.

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
Run a small starter HTTP service. Add a health endpoint, read a non-sensitive setting from an environment variable, inspect logs and test with curl.

## Stretch challenge
Add input validation and a basic automated test; explain missing configuration behaviour.

## Evidence to submit
Source code, run instructions, health endpoint and one test.

Add evidence to your own learning log or capstone repository. Redact identifiers and sensitive values. A short explanation is more useful than an unexplained screenshot.

## Safety and cleanup
Use dummy values. Do not put credentials in source code.

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
