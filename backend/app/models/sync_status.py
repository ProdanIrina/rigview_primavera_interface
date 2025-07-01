from pydantic import BaseModel

class SyncStatus(BaseModel):
    id: int
    timestamp: str
    direction: str
    sync_type: str
    status: str
    message: str
