# Week 10 Lab: Connect services across a network boundary

[← Practical labs](README.md) · [← Week 10 guide](../weeks/week-10.md) · [Starter app](starter-app/README.md)

## Mission
Use a Docker bridge network to connect two containers, then map concepts to VPCs, subnets, routes, ingress/egress and private services.

**Time:** 60–90 minutes · **Cost:** Free; Docker required

## Part A — Build the Week 6 image
```bash
cd curriculum/labs/starter-app
docker build -t cloud-track-demo:week-10 .
docker network create cloud-track-lab
docker network inspect cloud-track-lab
```

A user-defined bridge network provides container connectivity and DNS-based name resolution. It is not a full simulation of a cloud VPC.

## Part B — Start the API without a host port
```bash
docker run -d --name cloud-track-api --network cloud-track-lab cloud-track-demo:week-10
```

No `-p` option is used. The service is not published on a host port, but another container on the same network can reach it.

## Part C — Request it from a second container
```bash
docker run --rm --network cloud-track-lab curlimages/curl:latest -i http://cloud-track-api:8080/healthz
docker run --rm --network cloud-track-lab curlimages/curl:latest -i http://cloud-track-api:8080/api/info
```

Expected: HTTP 200. Docker DNS resolves `cloud-track-api`. If the diagnostic image cannot be downloaded, retry when connected or use an approved local diagnostic image.

## Part D — Compare host and container access
```bash
docker ps --format 'table {{.Names}}\t{{.Ports}}'
docker network inspect cloud-track-lab
docker rm -f cloud-track-api
docker run -d --name cloud-track-api --network cloud-track-lab -p 127.0.0.1:8080:8080 cloud-track-demo:week-10
curl -i http://127.0.0.1:8080/healthz
```

Loopback binding makes the example reachable from the local host, not all host interfaces. Do not expose services publicly to make a lab work.

## Core challenge
Add a second container and request `/api/info`. Draw the request path; label source, destination, network boundary, port, DNS name and host-port publication.

## Intermediate stretch
Disconnect the diagnostic container from the network and explain why it cannot reach the API. Reconnect and retry. Explain how cloud firewall rules differ from Docker network membership.

## Concept mapping
| Local concept | Cloud networking concept |
|---|---|
| User-defined Docker network | VPC/network |
| Container address | Workload network interface/address |
| Container DNS name | Internal service DNS |
| Published host port | Listener/forwarding path |
| Network membership | Network attachment and policy |

This is a conceptual mapping, not a claim Docker implements cloud subnets, routing tables, NAT or cloud firewall policy.

## Troubleshooting
Reuse an existing network if present. Inspect `docker ps -a` before removing a conflicting lab container. Check `docker logs cloud-track-api` if refused. Confirm both containers use `cloud-track-lab` if DNS fails.

## Cleanup
```bash
docker rm -f cloud-track-api 2>/dev/null || true
docker network rm cloud-track-lab
```

If the network is in use, inspect it and remove only lab containers. Do not prune all Docker resources.

## Evidence
Submit `week-10-evidence.md` with topology, successful request output, port-exposure explanation, one connectivity diagnosis and cleanup confirmation.
