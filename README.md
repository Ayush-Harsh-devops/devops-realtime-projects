# 🚀 DevOps Real-Time Projects — Ayush Harsh

> Production-grade DevOps portfolio | AWS | Kubernetes | Terraform | CI/CD | MLOps | Monitoring

[![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazon-aws&logoColor=white)](https://aws.amazon.com)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)](https://kubernetes.io)
[![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat&logo=terraform&logoColor=white)](https://terraform.io)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://docker.com)
[![ArgoCD](https://img.shields.io/badge/ArgoCD-EF7B4D?style=flat&logo=argo&logoColor=white)](https://argoproj.github.io)

---

## 👨‍💻 About
**Ayush Harsh** — DevOps Engineer with 3+ years of experience in cloud infrastructure, CI/CD automation, and Kubernetes deployments.

🏆 **Certifications:** AWS SAA-C03 | AZ-104 | AZ-400 | CKAD

📧 **Email:** harsh4ayush85@gmail.com

---

## 📂 Projects Overview

| # | Project | Tech Stack | Level |
|---|---------|-----------|-------|
| 01 | CI/CD Complete Pipeline | Jenkins, GitHub Actions, ArgoCD, EKS | ⭐⭐⭐⭐⭐ |
| 02 | IaC Multi-Environment AWS | Terraform, VPC, EKS, RDS | ⭐⭐⭐⭐⭐ |
| 03 | Kubernetes E-commerce App | Docker, Helm, ArgoCD, Prometheus | ⭐⭐⭐⭐⭐ |
| 04 | MLOps on Kubernetes | Python, MLflow, FastAPI, EKS | ⭐⭐⭐⭐⭐ |
| 05 | Monitoring & Observability | Prometheus, Grafana, Loki, Alertmanager | ⭐⭐⭐⭐⭐ |

---

## 🔄 Project 01 — CI/CD Complete Pipeline

**End-to-end CI/CD pipeline with GitOps deployment on AWS EKS**

Code Push → GitHub Actions (Trivy + SonarQube)
↓
Jenkins (Build + Quality Gate)
↓
Docker Build → AWS ECR
↓
ArgoCD GitOps → AWS EKS (Zero Downtime)

**Key Features:**
- ✅ Trivy security scanning — blocks Critical/High CVEs
- ✅ SonarQube code quality gates
- ✅ Multi-stage Docker builds (smaller images)
- ✅ GitOps with ArgoCD (auto sync + self heal)
- ✅ Zero downtime Rolling Updates
- ✅ HPA auto scaling (2-10 pods)

**Tech:** `Jenkins` `GitHub Actions` `ArgoCD` `Docker` `AWS ECR` `AWS EKS` `SonarQube` `Trivy`

---

## 🌍 Project 02 — IaC Multi-Environment AWS Terraform

**Production-grade AWS infrastructure with reusable Terraform modules**

modules/
vpc/ → VPC, Subnets, NAT Gateway
eks/ → EKS Cluster, Node Groups, IAM
rds/ → PostgreSQL, Secrets Manager
environments/
dev/  → t3.medium | 1 node
prod/ → t3.large  | 3 nodes | Multi-AZ

**Key Features:**

- ✅ Reusable Terraform modules
- ✅ Dev / Staging / Prod environments
- ✅ Remote state — S3 + DynamoDB lock
- ✅ Auto-generated passwords in Secrets Manager
- ✅ Multi-AZ RDS in Production
- ✅ Least privilege IAM roles

**Tech:** `Terraform` `AWS VPC` `AWS EKS` `AWS RDS` `S3` `DynamoDB` `Secrets Manager`

---

## ☸️ Project 03 — Kubernetes E-commerce App

**3-tier e-commerce app on AWS EKS with full GitOps and monitoring**

User → AWS ALB Ingress
↓
Frontend (React/Nginx) — 3 replicas
↓
Backend (Node.js API) — 3 replicas
↓
PostgreSQL + Redis Cache

**Key Features:**

- ✅ Multi-stage Docker builds
- ✅ Helm charts deployment
- ✅ ArgoCD GitOps auto sync
- ✅ HPA auto scaling (2-10 pods)
- ✅ Prometheus + Grafana monitoring
- ✅ AWS ALB Ingress Controller

**Tech:** `Docker` `Kubernetes` `Helm` `ArgoCD` `Prometheus` `Grafana` `AWS EKS` `Redis` `PostgreSQL`

---

## 🤖 Project 04 — MLOps on Kubernetes

**Production ML pipeline with experiment tracking and model serving**
Scikit-learn Training
↓
MLflow (Experiment Tracking + Registry)
↓
FastAPI (REST Model Serving)
↓
Docker → ECR → Kubernetes EKS
↓
Prometheus Metrics + HPA

**Key Features:**
- ✅ MLflow experiment tracking + model registry
- ✅ FastAPI REST endpoint for predictions
- ✅ Prometheus metrics on /metrics
- ✅ HPA auto scaling (2-8 pods)
- ✅ Zero downtime rolling updates
- ✅ AWS S3 artifact storage

**Tech:** `Python` `Scikit-learn` `MLflow` `FastAPI` `Docker` `Kubernetes` `AWS ECR` `AWS S3`

---

## 📊 Project 05 — Monitoring & Observability Stack

**Full-stack monitoring with metrics, logs, and intelligent alerting**
Apps + K8s Nodes
↓
Node Exporter + cAdvisor
↓
Prometheus (Metrics + Alert Rules)
↓
Alertmanager (Email Routing)
↓
Grafana (Dashboards)
Logs: Promtail → Loki → Grafana
**Key Features:**
- ✅ Infrastructure alerts — CPU/Memory/Disk
- ✅ Kubernetes alerts — Pod crash/Not ready
- ✅ Application alerts — Error rate/Response time
- ✅ Log aggregation — Loki + Promtail
- ✅ Email alerting via Alertmanager
- ✅ 15 days metrics retention

**Tech:** `Prometheus` `Grafana` `Alertmanager` `Loki` `Promtail` `Node Exporter` `cAdvisor`

---

## 🛠️ Complete Tech Stack

| Category | Tools |
|----------|-------|
| **CI/CD** | Jenkins, GitHub Actions, GitLab CI, Azure Pipelines, ArgoCD |
| **Cloud** | AWS (EKS, ECR, RDS, VPC, S3, IAM, Secrets Manager) |
| **Containers** | Docker, Kubernetes, Helm, GitOps |
| **IaC** | Terraform (Modules), Ansible |
| **Monitoring** | Prometheus, Grafana, Loki, Alertmanager, Datadog |
| **Security** | Trivy, SonarQube, AWS Secrets Manager |
| **ML** | Python, Scikit-learn, MLflow, FastAPI |
| **Database** | PostgreSQL, Redis |

---

## 🏆 Certifications

| Certification | Provider | Badge |
|--------------|----------|-------|
| AWS Solutions Architect Associate | Amazon Web Services | SAA-C03 |

---

## 📈 GitHub Stats

![Ayush's GitHub Stats](https://github-readme-stats.vercel.app/api?username=Ayush-Harsh-devops&show_icons=true&theme=dark)

---

*⭐ If you find these projects helpful, please consider giving a star!*
