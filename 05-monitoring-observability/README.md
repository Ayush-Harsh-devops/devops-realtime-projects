# 📊 Monitoring & Observability Stack

## 📌 Overview
Complete production monitoring stack with metrics,
logs, and alerting for Kubernetes workloads.

## 🏗️ Architecture

Applications + K8s Nodes
↓
Node Exporter + cAdvisor (Metrics)
↓
Prometheus (Scrape + Alert Rules)
↓
Alertmanager (Email Alerts)
↓
Grafana (Dashboards)
Logs: Promtail → Loki → Grafana

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Prometheus | Metrics Collection |
| Grafana | Dashboards + Visualization |
| Alertmanager | Alert Routing (Email) |
| Loki | Log Aggregation |
| Promtail | Log Shipping |
| Node Exporter | Host Metrics |
| cAdvisor | Container Metrics |

## ⚡ Key Features
- ✅ Infrastructure alerts (CPU/Memory/Disk)
- ✅ Kubernetes alerts (Pod crash/Not ready)
- ✅ Application alerts (Error rate/Response time)
- ✅ Log aggregation with Loki + Promtail
- ✅ Email alerting via Alertmanager
- ✅ 15 days metrics retention
- ✅ Pre-built Grafana dashboards

## 🚀 Quick Start
```bash
docker-compose up -d

# Access:
# Prometheus:   http://localhost:9090
# Grafana:      http://localhost:3000
# Alertmanager: http://localhost:9093
# Loki:         http://localhost:3100
```

## 👨‍💻 Author
**Ayush Harsh** | DevOps Engineer | CKAD | AWS SAA-C03
🔗 github.com/Ayush-Harsh-devops
