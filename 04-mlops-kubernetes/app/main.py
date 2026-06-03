from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
from prometheus_fastapi_instrumentator import Instrumentator
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="MLOps API — Ayush Harsh",
    description="Production ML Model serving on Kubernetes",
    version="1.0.0"
)

# Prometheus metrics
Instrumentator().instrument(app).expose(app)

# MLflow setup
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000")
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

class PredictionRequest(BaseModel):
    features: list[float]
    model_name: str = "production-model"

class PredictionResponse(BaseModel):
    prediction: float
    model_version: str
    status: str

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "mlops-api"}

@app.get("/ready")
async def ready():
    return {"status": "ready"}

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    try:
        model = mlflow.sklearn.load_model(
            f"models:/{request.model_name}/Production"
        )
        features = np.array(request.features).reshape(1, -1)
        prediction = model.predict(features)[0]
        logger.info(f"Prediction: {prediction}")
        return PredictionResponse(
            prediction=float(prediction),
            model_version="1.0.0",
            status="success"
        )
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/models")
async def list_models():
    client = mlflow.tracking.MlflowClient()
    models = client.search_registered_models()
    return {"models": [m.name for m in models]}
