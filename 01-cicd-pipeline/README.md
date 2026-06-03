# 🚀 CI/CD Complete Pipeline — Production Grade

## 📌 Overview
End-to-end CI/CD pipeline using Jenkins + GitHub Actions + ArgoCD
deploying Node.js app to AWS EKS with zero downtime.

## 🏗️ Architecture

Code Push → GitHub Actions (Trivy + SonarQube + Tests)
↓
Jenkins (Build + Quality Gate)
↓
Docker Build → Push to AWS ECR
↓
ArgoCD GitOps → AWS EKS (Zero Downtime)****

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Jenkins | Build & Orchestration |
| GitHub Actions | Security + Quality |
| SonarQube | Code Quality Gate |
| Trivy | Vulnerability Scanner |
| Docker | Multi-stage Build |
| AWS ECR | Container Registry |
| ArgoCD | GitOps Deployment |
| AWS EKS | Kubernetes Cluster |
| HPA | Auto Scaling |

## ⚡ Key Features
- ✅ Trivy security scan — blocks Critical/High CVEs
- ✅ SonarQube quality gate
- ✅ Multi-stage Docker build (smaller images)
- ✅ GitOps with ArgoCD (auto sync + self heal)
- ✅ Zero downtime Rolling Update
- ✅ HPA auto scaling (2-10 pods)
- ✅ Health + Readiness probes

## 👨‍💻 Author
**Ayush Harsh** | DevOps Engineer | CKAD | AWS SAA-C03
🔗 github.com/Ayush-Harsh-devops
