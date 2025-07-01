import os
import pyodbc
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

# Încarcă variabilele din .env
load_dotenv()
DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")

def get_db_conn():
    return pyodbc.connect(DB_CONNECTION_STRING)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =================== Login ===================

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
def login_user(data: LoginRequest):
    # Exemplu test user hardcodat
    if data.username == "testuser" and data.password == "testpass":
        return {"token": "test-token"}
    # Sau caută în baza de date
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

# =================== Dashboard Status ===================

class SyncStatus(BaseModel):
    id: int
    timestamp: str
    direction: str
    sync_type: str
    status: str
    message: str

@app.get("/status", response_model=List[SyncStatus])
def get_sync_status():
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, timestamp, direction, sync_type, status, message
        FROM sync_status
        ORDER BY timestamp DESC
    """)
    rows = cursor.fetchall()
    result = [
        SyncStatus(
            id=row.id,
            timestamp=row.timestamp.strftime("%Y-%m-%d %H:%M"),
            direction=row.direction,
            sync_type=row.sync_type,
            status=row.status,
            message=row.message
        )
        for row in rows
    ]
    cursor.close()
    conn.close()
    return result

# =================== Logs (Audit) ===================

class AppLog(BaseModel):
    date: str
    level: str
    component: str
    action: str
    initiated_by: str
    status: str
    message: str

@app.get("/logs", response_model=List[AppLog])
def get_logs():
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT date, level, component, action, initiated_by, status, message
        FROM app_log
        ORDER BY date DESC
    """)
    rows = cursor.fetchall()
    result = [
        AppLog(
            date=row.date.strftime("%Y-%m-%d %H:%M"),
            level=row.level,
            component=row.component,
            action=row.action,
            initiated_by=row.initiated_by,
            status=row.status,
            message=row.message
        )
        for row in rows
    ]
    cursor.close()
    conn.close()
    return result

# =================== Credentiale - exemplu ===================

class Credential(BaseModel):
    id: int
    username: str
    created_at: str

@app.get("/credentials", response_model=List[Credential])
def get_credentials():
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, username, created_at
        FROM credentials
        ORDER BY created_at DESC
    """)
    rows = cursor.fetchall()
    result = [
        Credential(
            id=row.id,
            username=row.username,
            created_at=row.created_at.strftime("%Y-%m-%d %H:%M")
        )
        for row in rows
    ]
    cursor.close()
    conn.close()
    return result

# =================== Health & Test endpoints ===================

@app.get("/")
def hello():
    return {"msg": "merge"}

@app.get("/ping")
def ping():
    return {"pong": True}
