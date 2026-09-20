from fastapi.testclient import TestClient
from app import app

client=TestClient(app)
sample={"records":[{"site":"LKO1","shift":"Day","units_processed":850,"planned_units":1000,"defects":35,"labor_hours":40,"backlog_units":620}]}

def test_health():
    assert client.get("/health").json()=={"status":"healthy"}

def test_summary_and_exceptions():
    summary=client.post("/analytics/summary",json=sample)
    assert summary.status_code==200
    assert summary.json()["plan_attainment"]==.85
    result=client.post("/analytics/exceptions",json=sample).json()
    assert result["exception_count"]==1
