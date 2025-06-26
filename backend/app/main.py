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

# =========== ACTIVITĂȚI (Primavera → RigView) ============

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

# =========== LOGURI MOCK (pentru Dashboard) ============

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

# =========== RIGVIEW → PRIMAVERA (export resurse, buget etc.) ============

class RigResource(BaseModel):
    rigname: str
    peloton_id: Optional[str]
    primavera_id: Optional[str]
    rig_type: Optional[str]

class BudgetType(BaseModel):
    uwi: str
    budget_type: str

class WellType(BaseModel):
    uwi: str
    well_type: str

class InitialConcept(BaseModel):
    uwi: str
    concept: str

@app.get("/rigs", response_model=List[RigResource])
def get_rigs():
    return [
        RigResource(rigname="Bega 1 HH 102", peloton_id="R102", primavera_id="EPRO-IAP R82", rig_type="TRANSFER"),
        RigResource(rigname="Dafora 2 - Bentec 350", peloton_id="R105", primavera_id="EPRO-IAP R85", rig_type="TRANSFER"),
    ]

@app.get("/budgets", response_model=List[BudgetType])
def get_budgets():
    return [
        BudgetType(uwi="UWI-101", budget_type="Dev"),
        BudgetType(uwi="UWI-102", budget_type="Drilling"),
    ]

@app.get("/welltypes", response_model=List[WellType])
def get_welltypes():
    return [
        WellType(uwi="UWI-101", well_type="Appraisal"),
        WellType(uwi="UWI-102", well_type="Development"),
    ]

@app.get("/concepts", response_model=List[InitialConcept])
def get_concepts():
    return [
        InitialConcept(uwi="UWI-101", concept="AAP"),
        InitialConcept(uwi="UWI-102", concept="Exploration"),
    ]

# =========== MOCK POST PRIMAVERA/UPDATE (ca să testezi orice push) ============

@app.post("/primavera/resource")
def add_resource_to_primavera(resource: RigResource):
    print("Resource to Primavera:", resource)
    return {"message": "Resource received"}

# =========== MOCK ENDPOINTURI GENERALE ============

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
