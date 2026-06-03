# 🤖 MLOps on Kubernetes — Python + MLflow + FastAPI + AWS EKS

## 📌 Overview
Production-grade MLOps pipeline with model training,
experiment tracking, and serving on Kubernetes.

## 🏗️ Architecture

Training Script (Scikit-learn)
↓
MLflow (Experiment Tracking + Model Registry)
↓
FastAPI (Model Serving API)
↓
Docker → AWS ECR → Kubernetes EKS
↓
Prometheus + Grafana (Monitoring)

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Python + Scikit-learn | ML Model Training |
| MLflow | Experiment Tracking + Registry |
| FastAPI | Model Serving API |
| Docker | Containerization |
| Kubernetes EKS | Production Deployment |
| HPA | Auto Scaling |
| Prometheus | Metrics Collection |
| AWS ECR | Container Registry |
| AWS S3 | Model Artifact Storage |

## ⚡ Key Features
- ✅ MLflow experiment tracking
- ✅ Model versioning + registry
- ✅ FastAPI REST endpoint for predictions
- ✅ Prometheus metrics on /metrics
- ✅ HPA auto scaling (2-8 pods)
- ✅ Zero downtime rolling updates
- ✅ Health + Readiness probes

## 🚀 Local Run
```bash
# Train model
python train/train.py

# Run API
uvicorn app.main:app --reload

# Test prediction
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

## 👨‍💻 Author
**Ayush Harsh** | DevOps Engineer | CKAD | AWS SAA-C03
🔗 github.com/Ayush-Harsh-devops
