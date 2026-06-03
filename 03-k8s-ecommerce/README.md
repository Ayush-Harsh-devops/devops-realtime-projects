# ☸️ E-commerce App — Docker & Kubernetes Production Deploy

## 📌 Overview
Full 3-tier e-commerce app containerized with Docker
and deployed on AWS EKS using Helm + ArgoCD GitOps
with Prometheus & Grafana monitoring.

## 🏗️ Architecture


User → AWS ALB Ingress
↓
Frontend (React/Nginx) — 3 replicas
↓
Backend (Node.js API) — 3 replicas
↓
PostgreSQL (RDS) + Redis (Cache)
Monitoring: Prometheus → Grafana
GitOps:     GitHub → ArgoCD → EKS

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Docker | Containerization |
| Docker Compose | Local Development |
| Kubernetes EKS | Production Orchestration |
| Helm | K8s Package Manager |
| ArgoCD | GitOps Deployment |
| Prometheus | Metrics Collection |
| Grafana | Monitoring Dashboard |
| AWS ALB | Load Balancer |
| HPA | Auto Scaling (2-10 pods) |

## ⚡ Key Features
- ✅ Multi-stage Docker builds
- ✅ Docker Compose local dev
- ✅ Helm charts deployment
- ✅ ArgoCD GitOps auto sync
- ✅ HPA auto scaling
- ✅ Zero downtime Rolling Updates
- ✅ Prometheus + Grafana monitoring
- ✅ AWS ALB Ingress Controller

## 🚀 Local Dev
```bash
cd docker
docker-compose up -d
# Frontend: http://localhost:80
# Backend:  http://localhost:3000
# Grafana:  http://localhost:3001
```

## 👨‍💻 Author
**Ayush Harsh** | DevOps Engineer | CKAD | AWS SAA-C03
🔗 github.com/Ayush-Harsh-devops
