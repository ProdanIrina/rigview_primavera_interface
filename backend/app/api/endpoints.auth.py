from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..database import get_db_conn

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login_user(data: LoginRequest):
    # 1. Test user rapid
    if data.username == "testuser" and data.password == "testpass":
        return {"token": "test-token"}

    # 2. Useri reali din SQL
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM credentials WHERE username = ? AND password = ?",
        (data.username, data.password)
    )
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row:
        return {"token": "jwt-or-mock-token"}
    raise HTTPException(status_code=401, detail="Credentiale invalide")
