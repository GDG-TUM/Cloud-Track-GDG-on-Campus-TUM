# Week 16 Lab: Demonstrate the system and reflect

[← Practical labs](README.md) · [← Week 16 guide](../weeks/week-16.md) · [Assessment rubric](../assessment.md)

## Mission
Present a working capstone, explain the engineering decisions behind it and show evidence from the 16-week journey. The objective is clarity and honest technical reasoning—not a sales pitch.

**Time:** 90-minute demo session plus preparation · **Cost:** Free; recorded or local demo is acceptable

## Part A — Prepare the demo environment
- Confirm the exact commit or release tag.
- Rehearse setup and the core user journey from a clean state.
- Verify the demo account contains synthetic data only.
- Check connectivity, display scaling, audio and required credentials.
- Prepare screenshots or a short recording as a fallback; redact private information.
- Have a local run path if a cloud endpoint becomes unavailable.
- Do not expose admin consoles, tokens, environment variables or private dashboards during screen sharing.

## Part B — Build a five-minute technical narrative
| Time | What to show |
|---:|---|
| 0:00–0:40 | Problem, intended user and scope |
| 0:40–1:30 | Architecture diagram and service choices |
| 1:30–2:45 | Core user journey working live |
| 2:45–3:30 | CI/build/deployment and data flow |
| 3:30–4:20 | Security and observability evidence |
| 4:20–5:00 | One failure, trade-off, limitation and next step |

Show one real command, test result, log excerpt or CI run. Do not spend the whole demo navigating slides.

## Part C — Prepare for questions
Be ready to answer:
- Why did you choose these services and not simpler alternatives?
- Where are the trust boundaries and who can access the data?
- How are secrets and workload identity handled?
- What happens when a dependency or service fails?
- How would you notice an incident and recover?
- What could incur cloud costs, and how do you clean it up?
- What is not production-ready yet?

If you do not know, say what evidence you would gather. Do not invent a feature, metric, test or deployment result.

## Part D — Peer feedback
Each reviewer records one strength supported by evidence, one unclear or unsupported claim, one practical improvement and one question they would ask before real users depended on it.

Give feedback on the work, not the person. Make space for beginners and solo contributors.

## Part E — Individual retrospective
Write a short reflection:
- What can I now do that I could not do in Week 1?
- Which debugging experience changed how I work?
- Which security or operational risk did I learn to recognize?
- What contribution did I personally make?
- What remains incomplete or unverified?
- What will I build or study next?

## Core challenge
Deliver the five-minute demo and submit the individual reflection plus links to the repository, architecture diagram and release evidence.

## Intermediate stretch
Present a short architecture decision record or incident postmortem. Explain a realistic next iteration, scaling constraint or security improvement without claiming the current student project is production-ready.

## Assessment
Use the [capstone rubric](../assessment.md). Evaluate functionality, architecture, engineering quality, security, observability, reproducibility and communication. A public URL is not a substitute for evidence. Local alternatives are valid when access to cloud services is constrained.

## Evidence
Submit repository and exact release commit/tag, architecture diagram, demo link or recording if available, CI/test and security/operations evidence, peer feedback and individual retrospective.

Do not publish secrets, personal data, private endpoint details or unredacted logs.
