# Assessment and Evidence Framework

[← Curriculum overview](README.md)

## Philosophy
Assessment rewards understanding and reproducible work, not copying commands or spending money. Members may demonstrate the same outcome with a local alternative when cloud access, hardware, connectivity or account eligibility is a barrier. Explain the alternative and its limitations.

## Weekly checkpoint
A checkpoint is complete when the member can:
1. Show the required artefact or command output.
2. Explain what they did and why.
3. Identify one failure mode, limitation or security/cost consideration.
4. Reproduce the result from their documentation, or explain what would be needed.

Suggested status: **Not started · In progress · Needs support · Complete**. This is a learning tracker, not a ranking system.

## Evidence examples
Git commits or reviewed PRs; sanitized terminal transcripts; Dockerfiles and run instructions; deployed endpoints without private data; architecture diagrams; CI runs and test results; sanitized Terraform plans; security findings and remediation; monitoring evidence; demo recordings and individual reflections.

Never submit API keys, access tokens, private keys, service-account JSON, passwords, personal data or unredacted billing details.

## Capstone rubric
| Dimension | Weight | Strong evidence |
|---|---:|---|
| Functionality and problem fit | 20% | Bounded problem; core flow works |
| Cloud architecture and deployment | 20% | Appropriate services, clear diagram, reproducible deployment |
| Engineering quality and automation | 15% | Readable code, tests, useful Git history, repeatable CI/build |
| Security and responsible operation | 15% | Least privilege, safe secrets, data protection, cleanup/cost awareness |
| Observability and troubleshooting | 10% | Useful logs/metrics, health checks, known failure response |
| Documentation and reproducibility | 10% | Another student can understand and run the project |
| Communication and reflection | 10% | Clear demo, honest trade-offs, individual reflection |

**Total: 100%.** A public URL is useful evidence, but does not replace security, documentation or explanation.

## Completion bands
- **Developing:** core workflow incomplete or requires substantial guidance.
- **Achieved:** outcome works and member can explain the main concepts.
- **Strong:** outcome is reproducible, tested and documented; trade-offs understood.
- **Extension:** meaningful improvement with a clear explanation of its value.

Use feedback to guide iteration. Do not use public leaderboards to shame beginners or compare members with different access to devices and connectivity.
