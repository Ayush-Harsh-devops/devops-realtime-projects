FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.11-slim AS production
WORKDIR /app
RUN addgroup --gid 1001 mlops && adduser --uid 1001 --gid 1001 --no-create-home mluser
COPY --from=builder /root/.local /home/mluser/.local
COPY --chown=mluser:mlops . .
USER mluser
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s \
  CMD curl -f http://localhost:8000/health || exit 1
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
