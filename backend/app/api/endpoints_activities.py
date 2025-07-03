from fastapi import APIRouter, HTTPException
from app.services.primavera_client import fetch_all_activities

router = APIRouter()

@router.get("/primavera/activities")
def get_primavera_activities():
    try:
        return fetch_all_activities()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
