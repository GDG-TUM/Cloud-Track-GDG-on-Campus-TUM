# Week 8 Lab: Deploy the container to Cloud Run

[← Practical labs](README.md) · [← Week 8 guide](../weeks/week-08.md) · [Starter app](starter-app/README.md)

## Mission
Build the Week 6 container, publish it to Artifact Registry and deploy it as a Cloud Run service. Verify the endpoint and logs, then remove the resources created for the lab.

**Time:** 60–90 minutes plus build/deploy wait time  
**Cost:** May incur charges. This lab is optional unless the Track Lead provides an approved shared project.

## Mandatory pre-deployment gate

Do not proceed until all are true:
- [ ] The Track Lead/project owner has approved the project and deployment window.
- [ ] You know who pays for the project and have checked current pricing and quotas.
- [ ] You have permission to create/use Artifact Registry and Cloud Run resources.
- [ ] You have an agreed region and service name.
- [ ] You understand that budget notifications are not hard spending caps.
- [ ] You have a cleanup owner and time to verify deletion.

If any item is unclear, complete the local alternative below. Never attach personal billing details to finish a student lab.

## Part A — Confirm project and tools

```bash
gcloud version
gcloud auth list
gcloud config get-value project
docker version
```

Confirm the active account and project are the approved ones. Set variables in your shell, replacing the placeholders:

```bash
export PROJECT_ID="YOUR_APPROVED_PROJECT_ID"
export REGION="YOUR_APPROVED_REGION"
export REPOSITORY="cloud-track-labs"
export IMAGE="cloud-track-demo"
export SERVICE="cloud-track-demo"
```

Verify before continuing:

```bash
printf 'Project: %s\nRegion: %s\n' "$PROJECT_ID" "$REGION"
gcloud projects describe "$PROJECT_ID" --format='value(projectId)'
```

The displayed project ID must match exactly. Do not share your shell transcript if it contains private identifiers.

## Part B — Enable the required APIs

Only with project-owner approval:

```bash
gcloud services enable \
  run.googleapis.com \
  artifactregistry.googleapis.com \
  cloudbuild.googleapis.com \
  --project="$PROJECT_ID"
```

API enablement can have billing implications through dependent services. Ask the owner if the command reports missing permissions.

## Part C — Create an Artifact Registry Docker repository

Check whether the repository already exists:

```bash
gcloud artifacts repositories list \
  --project="$PROJECT_ID" --location="$REGION"
```

If it does not exist and the owner approves, create it:

```bash
gcloud artifacts repositories create "$REPOSITORY" \
  --repository-format=docker \
  --location="$REGION" \
  --description="GDG TUM Cloud Track learning images" \
  --project="$PROJECT_ID"
```

Do not create duplicate repositories. Image storage can continue to incur charges even after a Cloud Run service is deleted.

## Part D — Build and push the image

From the starter application directory:

```bash
cd curriculum/labs/starter-app
gcloud auth configure-docker "$REGION-docker.pkg.dev"
docker build -t "$REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE:week-08" .
docker push "$REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE:week-08"
```

Expected: Docker reports a successful push and an image digest. Record the digest for your evidence, but do not expose private project details publicly.

## Part E — Deploy to Cloud Run

Confirm the image reference and deploy:

```bash
gcloud run deploy "$SERVICE" \
  --image="$REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE:week-08" \
  --region="$REGION" \
  --project="$PROJECT_ID" \
  --port=8080 \
  --memory=512Mi \
  --cpu=1 \
  --min=0 \
  --max=2 \
  --set-env-vars="APP_MESSAGE=Hello from Cloud Run,APP_VERSION=0.4.0" \
  --allow-unauthenticated
```

The example uses a public endpoint so members can test it without setting up identity federation. It returns only synthetic demo data and is not an authenticated production application. If the project policy disallows public invocations, remove `--allow-unauthenticated` and follow the facilitator's private-service access instructions.

The example uses 512 MiB with 1 vCPU, a supported starting configuration. Cloud Run CLI flags and available settings can change. Check `gcloud run deploy --help` and the [Cloud Run deployment guide](https://docs.cloud.google.com/run/docs/deploying) before the cohort uses this lab. Source deployments and Artifact Registry behaviour are described in the [Cloud Run source deployment guide](https://docs.cloud.google.com/run/docs/deploying-source-code).

## Part F — Verify the deployment

```bash
gcloud run services describe "$SERVICE" \
  --region="$REGION" --project="$PROJECT_ID" \
  --format='value(status.url)'
```

Copy the returned URL into a shell variable:

```bash
export SERVICE_URL="PASTE_THE_RETURNED_URL_HERE"
curl -i "$SERVICE_URL/healthz"
curl -i "$SERVICE_URL/api/info"
```

Expected: HTTP 200 from both endpoints. Confirm the info response contains the configured message/version.

Inspect recent logs:

```bash
gcloud run services logs read "$SERVICE" \
  --region="$REGION" --project="$PROJECT_ID" --limit=20
```

Do not paste logs containing private identifiers into public issues.

## Core challenge
Deploy a second revision with a different non-sensitive `APP_MESSAGE`. Inspect the revisions and explain how Cloud Run revisions relate to immutable container images and traffic.

## Intermediate stretch
Deploy without public access in a facilitator-controlled project. Use an approved authenticated invocation method and explain the difference between invocation permission and the service's runtime identity.

## Local alternative — no cloud account or billing

From `curriculum/labs/starter-app`:

```bash
docker build -t cloud-track-demo:week-08-local .
docker run -d --name cloud-track-demo-local -p 8080:8080 cloud-track-demo:week-08-local
curl -i http://localhost:8080/healthz
curl -i http://localhost:8080/api/info
docker logs cloud-track-demo-local
docker stop cloud-track-demo-local
docker rm cloud-track-demo-local
```

Draw the deployment architecture and describe which steps would change when moving from local Docker to Cloud Run. This is valid evidence when cloud access is unavailable.

## Troubleshooting
- **API not enabled:** ask the project owner to approve and enable the required API.
- **Permission denied on push:** verify Artifact Registry Writer access for the deploying identity on the target repository.
- **Build fails:** check Cloud Build permissions and inspect the first failing build step.
- **Image not found:** confirm region, project, repository, image name and tag all match.
- **Container fails startup:** inspect Cloud Run logs; confirm the process listens on `0.0.0.0` and the `PORT` environment variable (8080 here).
- **Health request returns 404:** verify the path is `/healthz` and the deployed image contains the latest app code.
- **Public access is blocked:** follow organization policy; do not try to bypass it by changing project policy.

## Cleanup — do not skip

Delete the service:

```bash
gcloud run services delete "$SERVICE" \
  --region="$REGION" --project="$PROJECT_ID"
```

If the project owner confirms that this image tag belongs only to your lab, remove that artifact:

```bash
gcloud artifacts docker images delete \
  "$REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY/$IMAGE:week-08" \
  --delete-tags --quiet --project="$PROJECT_ID"
```

This deletes the image version/tag referenced by the command. Do not delete a shared repository that contains other members' images. If the image is shared, leave it in place and record that the owner is responsible for retention.

Verify the service is gone:

```bash
gcloud run services list --region="$REGION" --project="$PROJECT_ID"
gcloud artifacts repositories list --location="$REGION" --project="$PROJECT_ID"
```

The repository may remain and continue to incur image-storage costs. Coordinate whether it is shared or dedicated before deleting it. Record cleanup completion with the project owner.

## Evidence
Submit `week-08-evidence.md` with:
- Sanitized project/region reference (or state that you used the local alternative).
- Image build and push outcome.
- Cloud Run URL only if the project owner approves sharing it.
- Health/info endpoint results.
- One log observation.
- Revision and scaling explanation.
- Cleanup confirmation and any remaining shared resources.
