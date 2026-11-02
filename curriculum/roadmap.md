# 16-Week Cloud Engineering Roadmap

[← Curriculum overview](README.md)

| Week | Theme | Core topics | Required evidence |
|---:|---|---|---|
| 1 | Cloud concepts and safe setup | Service models, regions/zones, shared responsibility, projects, billing, IAM | Architecture sketch and safe-account checklist |
| 2 | Linux and CLI foundations | Files, permissions, processes, pipes, environment, SSH, package management | CLI task log and shell challenge |
| 3 | Networking foundations | IPs, ports, DNS, HTTP/HTTPS, TCP/UDP, routing, subnet intuition | Request journey and diagnostic notes |
| 4 | Git collaboration | Commits, branches, remotes, pull requests, reviews, issues | Reviewed pull request |
| 5 | Application runtime | HTTP service, environment variables, config, health endpoints, logs | Runnable web/API service |
| 6 | Docker workflows | Images, containers, Dockerfile, ports, volumes, networks, Compose | Reproducible container build |
| 7 | Google Cloud and IAM | Resource hierarchy, APIs, gcloud, service accounts, roles | Project setup and least-privilege exercise |
| 8 | Cloud compute | Cloud Run, deployment, revisions, environment configuration, scaling | Deployed endpoint and cleanup record |
| 9 | Storage and databases | Object storage, relational vs NoSQL, persistence, data safety | Application uses a data service |
| 10 | Cloud networking | VPCs, subnets, ingress/egress, firewall rules, public/private boundaries | Network and data-flow diagram |
| 11 | CI/CD | GitHub Actions, triggers, jobs, tests, build, secrets, gates | CI workflow on pull requests |
| 12 | Infrastructure as Code | Terraform providers, resources, variables, state, plan/apply/destroy | Terraform configuration and lifecycle guide |
| 13 | Cloud security | IAM, workload identity, secrets, audit logs, image/dependency hygiene | Security review and remediation |
| 14 | Observability and reliability | Logs, metrics, alerts, health checks, failure modes, cost | Monitoring evidence and runbook |
| 15 | Capstone hardening | Architecture review, threat modelling, tests, readiness, documentation | Release candidate and peer review |
| 16 | Demo and retrospective | Demo, architecture explanation, troubleshooting, lessons | Portfolio artefact and reflection |

## Dependency logic
Weeks 1–4 establish the operating environment and shared vocabulary. Weeks 5–6 create an application that can run consistently before deployment. Weeks 7–10 teach the cloud platform and infrastructure around it. Weeks 11–12 automate delivery and infrastructure. Weeks 13–14 apply security and operational practices. Weeks 15–16 consolidate evidence and communication.

## Continuous capstone
Choose a small problem by Week 4. Start a local app in Week 5, containerize in Week 6, deploy in Week 8, connect data by Week 9, automate and provision in Weeks 11–12, then harden and observe in Weeks 13–15. Keep scope deliberately small enough to finish.

## Weekly time budget
| Activity | Typical time |
|---|---:|
| Facilitated session | 90 minutes |
| Guided lab / core challenge | 60–90 minutes |
| Independent practice and notes | 60–90 minutes |
| **Total** | **3.5–4.5 hours** |

Prioritize the core outcome over optional extensions.
