[← Back to Cloud Track home](../README.md)


# Stage 5: Security and Observability

**Goal:** Make your project safe to run and easy to understand when something breaks.

**Matching session:** [week-09-security-and-monitoring](../weekly-sessions/week-09-security-and-monitoring/README.md)

## What you will learn
- Least privilege and service accounts
- Secret management (never in code, never in Git)
- Audit logs: who did what, and when
- Logging and monitoring: logs, metrics, alerts
- Common cloud mistakes: public buckets, over-permissive roles, leaked keys

## Hands-on
1. Review your project's IAM roles and remove anything unneeded.
2. Store one secret in Secret Manager and read it from an app.
3. Create an alert for something that matters (errors or unexpected cost).
4. Run through the [security checklist](../resources/cloud-security-checklist.md).

## Free resources
See [resources](../resources/free-resources.md) for official docs, labs and tutorials.

## ✅ Checkpoint
- Can I name three common cloud security mistakes?
- Where would I look to find out who changed a resource?
- Would I know if my app started failing?

If you can answer these, move to the next stage. If not, revisit the topics or ask in the track channel.

[← Learning path overview](README.md)
