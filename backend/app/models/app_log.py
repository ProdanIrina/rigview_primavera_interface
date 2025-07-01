from pydantic import BaseModel

class AppLog(BaseModel):
    date: str
    level: str
    component: str
    action: str
    initiated_by: str
    status: str
    message: str
