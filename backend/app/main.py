from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import endpoints_status, endpoints_logs, endpoints_auth, endpoints_credential, endpoints_activities

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(endpoints_status.router)
app.include_router(endpoints_logs.router)
app.include_router(endpoints_auth.router)
app.include_router(endpoints_credential.router)
app.include_router(endpoints_activities.router)

# =================== Health & Test endpoints ===================

@app.get("/")
def hello():
    return {"msg": "merge"}

@app.get("/ping")
def ping():
    return {"pong": True}
