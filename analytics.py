from typing import Iterable
from schemas import OperationRecord

def summarize(rows: Iterable[OperationRecord]):
    rows=list(rows)
    if not rows:
        return {"records":0,"total_units":0,"plan_attainment":0,"defect_rate":0,"units_per_labor_hour":0}
    units=sum(r.units_processed for r in rows)
    plan=sum(r.planned_units for r in rows)
    defects=sum(r.defects for r in rows)
    hours=sum(r.labor_hours for r in rows)
    return {"records":len(rows),"total_units":units,"plan_attainment":round(units/plan,4) if plan else 0,"defect_rate":round(defects/units,4) if units else 0,"units_per_labor_hour":round(units/hours,2) if hours else 0}

def exceptions(rows: Iterable[OperationRecord]):
    result=[]
    for r in rows:
        attainment=r.units_processed/r.planned_units if r.planned_units else 0
        defect_rate=r.defects/r.units_processed if r.units_processed else 0
        if attainment<.9 or defect_rate>.03 or r.backlog_units>500:
            result.append({"site":r.site,"shift":r.shift,"attainment":round(attainment,3),"defect_rate":round(defect_rate,3),"backlog_units":r.backlog_units})
    return result
