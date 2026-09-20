# Dockerized Operations Analytics API

A production-style FastAPI service packaged with Docker. It calculates fulfillment KPIs and exposes health, summary and exception endpoints.

## Endpoints
- `GET /health` — container health
- `POST /analytics/summary` — throughput, plan attainment and defect KPIs
- `POST /analytics/exceptions` — rows requiring operational attention
- `GET /docs` — interactive OpenAPI documentation

## Run with Docker
```bash
docker compose up --build
```
Open http://localhost:8000/docs.

## Run without Docker
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Test
```bash
pytest
```

## Technology
Python · FastAPI · Pydantic · Docker · pytest

Original portfolio implementation demonstrating deployable analytics engineering.
