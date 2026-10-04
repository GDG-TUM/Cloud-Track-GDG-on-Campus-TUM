[← Back to Cloud Track home](../../README.md)


# Week 3: Compute and containers

**Date:** 26 Oct (draft; confirm time and venue in the track channel)

**Goal:** Put a container on the internet.

## Learning objectives
By the end you should be able to:
- Compare VMs and Cloud Run
- Deploy a container to Cloud Run
- Clean up cloud resources

## Before the session
- [ ] Docker working
- [ ] `gcloud` installed and logged in
- [ ] Read [Stage 3](../../learning-path/03-build-and-deploy.md)

## Agenda
1. Compute options overview (20 min)
2. Demo: deploy to Cloud Run (20 min)
3. Hands-on: deploy your own app (40 min)
4. Cleanup and cost check (10 min)

## Hands-on reference
```bash
# Deploy from the folder containing your app
gcloud run deploy my-app --source . --region REGION --allow-unauthenticated

# Clean up when finished
gcloud run services delete my-app --region REGION
```
> `--allow-unauthenticated` makes the service public. Use it only for demos and delete it afterwards. Pick a region close to you that your account supports.

## 🏁 Take-home challenge
- [ ] Deploy a small app and share the URL in the track channel
- [ ] Add a short `README` to your app repo explaining what it does
- [ ] Delete the service and confirm no resources are left running

Post your result or questions in the track channel, or open an issue.

## 📝 Session notes
Add slides, links, recordings and key takeaways here after the session (via pull request).

- Slides: _to be added_
- Recording: _to be added_
- Extra resources: _to be added_

---
[← Week 2](../week-02-tools-of-the-trade/README.md) | [All sessions](../README.md) | [Week 4 →](../week-04-agentic-ai-study-jam/README.md)
