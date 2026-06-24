# Homelab TaskTracker v2

A production-style 3-tier task tracker application built for DevOps, Kubernetes, CI/CD, and GitOps practice.

## Project Goal

Build a task tracker app from scratch and deploy it like a real production application.

Users should be able to:

- Create tasks
- View tasks
- Mark tasks complete
- Delete tasks

## Architecture

Browser
→ Frontend
→ Backend API
→ PostgreSQL Database

## Tech Stack

- Frontend: React or simple HTML/JavaScript
- Backend: Python FastAPI
- Database: PostgreSQL
- Containers: Docker
- Local orchestration: Docker Compose
- Kubernetes: Proxmox Kubernetes cluster
- CI/CD: GitHub Actions
- GitOps: Argo CD
- Registry: Docker Hub

## Project Stages

1. Project planning
2. Backend API locally
3. PostgreSQL locally
4. Frontend locally
5. Dockerize services
6. Docker Compose
7. Kubernetes manifests
8. Kustomize base and overlays
9. CI/CD with GitHub Actions
10. GitOps with Argo CD
11. Ingress
12. Monitoring and backups
