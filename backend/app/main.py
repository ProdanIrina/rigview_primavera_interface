from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta
import os

# =============================
# FASTAPI + CORS
# =============================

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =============================
# ENV
# =============================

JWT_SECRET = os.getenv("JWT_SECRET", "testjwtsecret")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

# =============================
# MODELE
# =============================

class LoginRequest(BaseModel):
    username: str
    password: str
    remember: bool = False

class Activity(BaseModel):
    activity_id: str
    name: str
    uwi: str
    start: str
    finish: str
    status: str
    rig_view_code: str
    gate: str

# =============================
# ENDPOINTURI
# =============================

@app.post("/login")
def login_user(data: LoginRequest):
    # === VALIDARE MOCK ===
    if not (
        (data.username == "admin" and data.password == "test123")
        or (data.username == "testuser" and data.password == "testpass")
    ):
        raise HTTPException(status_code=401, detail="Credentiale invalide")

    # === GENERARE JWT ===
    token_payload = {
        "sub": data.username,
        "exp": datetime.utcnow() + timedelta(hours=12)
    }
    token = jwt.encode(token_payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    # În viitor aici poți salva credentiale dacă vrei

    return {"token": token}

@app.get("/sync/activities")
def get_filtered_activities():
    # mock demo
    return [
        {
            "activity_id": "ACT001",
            "name": "Drilling activity",
            "uwi": "UWI-123",
            "start": "2025-07-01",
            "finish": "2025-07-10",
            "status": "Not Started",
            "rig_view_code": "S",
            "gate": "G1"
        },
        {
            "activity_id": "ACT002",
            "name": "Flowline execution",
            "uwi": "UWI-124",
            "start": "2025-07-05",
            "finish": "2025-07-15",
            "status": "In Progress",
            "rig_view_code": "AR",
            "gate": "G2"
        }
    ]

@app.get("/")
def hello():
    return {"msg": "merge"}

@app.get("/ping")
def ping():
    return {"pong": True}

# Adaugă alte endpointuri după ce ai DB și ai nevoie
