from pydantic import BaseModel,Field

class OperationRecord(BaseModel):
    site:str=Field(min_length=1)
    shift:str=Field(min_length=1)
    units_processed:int=Field(ge=0)
    planned_units:int=Field(gt=0)
    defects:int=Field(ge=0)
    labor_hours:float=Field(gt=0)
    backlog_units:int=Field(ge=0)

class Batch(BaseModel):
    records:list[OperationRecord]
