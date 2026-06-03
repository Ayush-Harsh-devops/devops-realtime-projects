# 🌍 IaC Multi-Environment AWS — Terraform

## 📌 Overview
Production-grade AWS infrastructure using reusable Terraform modules.
Manages Dev, Staging, and Prod environments from single codebase.

## 🏗️ Architecture

environments/
dev/   → t3.medium | 1 node  | db.t3.micro
prod/  → t3.large  | 3 nodes | db.t3.small
modules/
vpc/   → VPC, Subnets, NAT Gateway, Route Tables
eks/   → EKS Cluster, Node Groups, IAM Roles
rds/   → PostgreSQL, Security Groups, Secrets Manager

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Terraform | Infrastructure as Code |
| AWS VPC | Networking |
| AWS EKS | Kubernetes Cluster |
| AWS RDS | PostgreSQL Database |
| AWS Secrets Manager | Password Management |
| S3 + DynamoDB | Remote State + Lock |

## ⚡ Key Features
- ✅ Reusable Terraform modules
- ✅ Multi-environment (Dev/Staging/Prod)
- ✅ Remote state S3 + DynamoDB lock
- ✅ Auto-generated passwords in Secrets Manager
- ✅ Multi-AZ RDS in Production
- ✅ Least privilege IAM roles

## 🚀 Deploy
```bash
cd environments/dev
terraform init
terraform plan -var-file="terraform.tfvars"
terraform apply -var-file="terraform.tfvars"
```

## 👨‍💻 Author
**Ayush Harsh** | DevOps Engineer | CKAD | AWS SAA-C03
🔗 github.com/Ayush-Harsh-devops
