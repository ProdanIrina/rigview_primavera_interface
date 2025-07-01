from pydantic import BaseModel
from typing import Optional

class PrimaveraActivity(BaseModel):
    activity_id: str
    name: str
    uwi: Optional[str]
    start: str
    finish: str
    status: str
    rig_view_code: str
    project_status: str

class RigViewActivity(BaseModel):
    activity_id: str
    gate: str
    uwi: str
    start_date: str
    complete_date: str
    status: str
    rig_view: str
