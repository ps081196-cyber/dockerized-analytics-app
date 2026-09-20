from fastapi import FastAPI
from analytics import exceptions,summarize
from schemas import Batch

app=FastAPI(title="Operations Analytics API",version="1.0.0",description="Container-ready fulfillment KPI service")

@app.get("/health")
def health():
    return {"status":"healthy"}

@app.post("/analytics/summary")
def analytics_summary(batch:Batch):
    return summarize(batch.records)

@app.post("/analytics/exceptions")
def analytics_exceptions(batch:Batch):
    rows=exceptions(batch.records)
    return {"exception_count":len(rows),"exceptions":rows}
