# Week 6 Lab: Containerize the Cloud Track API

[← Practical labs](README.md) · [← Week 6 guide](../weeks/week-06.md) · [Starter app](starter-app/README.md)

## Mission
Build a Docker image for the Week 5 API, run it with a port mapping, inspect its logs and configuration, then remove the container safely.

**Time:** 60–90 minutes · **Cost:** Free locally (image downloads use network/data)

## Prerequisites
- Docker Engine or Docker Desktop running.
- Complete Week 5.
- Work from `curriculum/labs/starter-app`.

Check:

```bash
docker version
docker info
```

If `docker info` cannot connect to the daemon, start Docker using the normal method for your operating system before continuing. Do not run every Docker command with sudo as a default workaround.

## Part A — Build the image

```bash
docker build -t cloud-track-demo:week-06 .
docker image ls cloud-track-demo
```

Expected: a local image tagged `cloud-track-demo:week-06`.

Inspect its configuration:

```bash
docker image inspect cloud-track-demo:week-06 --format 'User={{.Config.User}} ExposedPorts={{json .Config.ExposedPorts}} Cmd={{json .Config.Cmd}}'
```

Expected: the configured user is `appuser`, the image exposes port 8080 and starts `python app.py`.

## Part B — Run the container

Stop the Week 5 local Python server with Ctrl+C before publishing host port 8080. If another service already uses that port, use a different host port as shown in Part D.

```bash
docker run -d --name cloud-track-demo -p 8080:8080 \
  -e APP_MESSAGE="Hello from Docker" \
  -e APP_VERSION="0.3.0" \
  cloud-track-demo:week-06
```

Check:

```bash
docker ps
docker logs cloud-track-demo
curl -i http://localhost:8080/healthz
curl -i http://localhost:8080/api/info
```

Expected: container is running, logs show startup and requests, health endpoint returns HTTP 200 and info contains the configured message.

The left side of `-p 8080:8080` is the host port; the right side is the container port.

## Part C — Inspect the container

```bash
docker inspect cloud-track-demo --format 'Status={{.State.Status}} ExitCode={{.State.ExitCode}}'
docker exec cloud-track-demo id
docker stats --no-stream cloud-track-demo
```

Expected: status is running; `id` shows the non-root application user; resource statistics are reported.

## Part D — Test port mapping

Stop and remove the container:

```bash
docker stop cloud-track-demo
docker rm cloud-track-demo
```

Run it on a different host port:

```bash
docker run -d --name cloud-track-demo -p 8081:8080 cloud-track-demo:week-06
curl -i http://localhost:8081/healthz
```

The app still listens on 8080 inside the container. Only the host-side port changed.

## Part E — Image and container are different

- An **image** is the packaged template used to create containers.
- A **container** is a running (or stopped) instance created from an image.
- Removing a container does not automatically remove its image.

Inspect:

```bash
docker ps -a
docker image ls cloud-track-demo
```

## Core challenge
Build a second tag for the same image and run two instances simultaneously on different host ports. Verify each responds. Use distinct container names and remove both when done.

## Intermediate stretch
Improve the Dockerfile:
- Add a `HEALTHCHECK` using Python's standard library.
- Explain why the image runs as a non-root user.
- Compare the image size before and after any change.
- Explain why secrets must not be passed through Dockerfile `ENV`, `ARG` or copied into image layers.

Do not add credentials to test the secrets warning.

## Troubleshooting
- **Cannot connect to Docker daemon:** start the service/desktop application and retry `docker info`.
- **Port already allocated:** identify your own container with `docker ps`; stop it, or choose another host port such as 8081.
- **Container exits immediately:** inspect `docker ps -a` and `docker logs cloud-track-demo`.
- **Image build fails:** confirm current directory contains `Dockerfile` and `app.py`; inspect the first build error.
- **Permission denied on Linux:** check Docker's documented installation and group guidance for your distribution. Avoid broad permission changes.

## Evidence
Submit `week-06-evidence.md` with Docker version, build command, image inspection, run command, endpoint output, log excerpt, port-mapping explanation and cleanup confirmation.

## Cleanup
Run:

```bash
docker stop cloud-track-demo
docker rm cloud-track-demo
docker image rm cloud-track-demo:week-06
```

If you created extra tags/containers for the stretch task, remove those too. Do not run `docker system prune -a` as a routine cleanup command; it may remove unrelated images and build cache.
