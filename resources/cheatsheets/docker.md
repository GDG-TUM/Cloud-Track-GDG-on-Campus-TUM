[← Back to Cloud Track home](../../README.md)

# Docker Cheat Sheet

```bash
docker build -t myapp .              # build an image
docker run -p 8080:8080 myapp        # run and publish a port
docker run -d --name web myapp       # run in the background
docker ps                            # running containers
docker ps -a                         # all containers
docker logs web                      # see output
docker stop web && docker rm web     # stop and remove
docker images                        # list images
docker rmi myapp                     # remove an image
docker system prune                  # clean unused data (careful)
```
**Tiny Dockerfile example:**
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

[← All resources](../README.md)
