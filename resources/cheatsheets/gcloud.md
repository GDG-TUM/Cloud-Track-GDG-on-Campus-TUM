[← Back to Cloud Track home](../../README.md)

# gcloud (Google Cloud CLI) Cheat Sheet

```bash
gcloud auth login                              # log in
gcloud projects list                           # your projects
gcloud config set project PROJECT_ID           # choose a project
gcloud config list                             # current config
gcloud services enable run.googleapis.com      # enable an API
gcloud run deploy NAME --source . --region REGION
gcloud run services list
gcloud run services delete NAME --region REGION
gcloud storage buckets list
gcloud iam service-accounts list
gcloud logging read "severity>=ERROR" --limit 20
```
Add `--help` to any command for details. **Cloud Shell** in the console has `gcloud` preinstalled.

[← All resources](../README.md)
