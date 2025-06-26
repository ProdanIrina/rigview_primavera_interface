from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta
from typing import List, Optional
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========== JWT LOGIN MOCK ============

JWT_SECRET = os.getenv("JWT_SECRET", "testjwtsecret")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

class LoginRequest(BaseModel):
    username: str
    password: str
    remember: bool = False

@app.post("/login")
def login_user(data: LoginRequest):
    if not (
        (data.username == "admin" and data.password == "test123")
        or (data.username == "testuser" and data.password == "testpass")
    ):
        raise HTTPException(status_code=401, detail="Credentiale invalide")

    token_payload = {
        "sub": data.username,
        "exp": datetime.utcnow() + timedelta(hours=12)
    }
    token = jwt.encode(token_payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"token": token}

# =========== ACTIVITY SYNC LOGIC ============

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

def filter_and_map_activities(activities: List[PrimaveraActivity]) -> List[RigViewActivity]:
    filtered = []
    for act in activities:
        if act.project_status in ["Completed", "Canceled"]:
            continue
        if act.rig_view_code not in ("S", "AR"):
            continue
        if not act.uwi:
            continue
        filtered.append(RigViewActivity(
            activity_id=act.activity_id,
            gate=act.name,
            uwi=act.uwi,
            start_date=act.start,
            complete_date=act.finish,
            status=act.status,
            rig_view=act.rig_view_code,
        ))
    return filtered

@app.get("/sync/activities", response_model=List[RigViewActivity])
def get_activities():
    # MOCK: Replace with DB/API data when ready!
    activities = [
        PrimaveraActivity(
            activity_id="A1010", name="Land rental for access road...", uwi="123", start="2024-07-01",
            finish="2024-07-05", status="Not Started", rig_view_code="S", project_status="Active"
        ),
        PrimaveraActivity(
            activity_id="A1200", name="Flowline execution", uwi="234", start="2024-08-01",
            finish="2024-08-05", status="Completed", rig_view_code="AR", project_status="Completed"
        ),
        PrimaveraActivity(
            activity_id="A1210", name="Drilling activity", uwi="999", start="2024-09-01",
            finish="2024-09-05", status="In Progress", rig_view_code="AR", project_status="Active"
        ),
        PrimaveraActivity(
            activity_id="A1300", name="Some other activity", uwi=None, start="2024-10-01",
            finish="2024-10-05", status="Not Started", rig_view_code="S", project_status="Active"
        ),
    ]
    return filter_and_map_activities(activities)

# =========== LOGURI MOCK ============

class SyncLog(BaseModel):
    date: str
    status: str  # "success" | "error" | "in_progress"
    message: str

@app.get("/logs", response_model=List[SyncLog])
def get_logs():
    return [
        SyncLog(
            date="2024-06-27 08:00",
            status="in_progress",
            message="Sincronizare pornită."
        ),
        SyncLog(
            date="2024-06-27 08:01",
            status="error",
            message="Conexiune eșuată la API Primavera."
        ),
        SyncLog(
            date="2024-06-27 08:02",
            status="success",
            message="Sincronizare reușită."
        ),
    ]

# =========== ENDPOINTS MOCK RIGVIEW/INTERFATA ============

@app.post("/update-rig")
def update_rig_allocation(data: dict = Body(...)):
    print("Primit de la RigView:", data)
    return {"message": "Rig received"}

@app.post("/sync/manual")
def manual_sync():
    print("Sincronizare manuală pornită!")
    return {"message": "Sincronizare pornită"}

@app.get("/")
def hello():
    return {"msg": "merge"}

@app.get("/ping")
def ping():
    return {"pong": True}
