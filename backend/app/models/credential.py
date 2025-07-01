from pydantic import BaseModel

class Credential(BaseModel):
    id: int
    username: str
    created_at: str
