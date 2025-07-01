from fastapi import APIRouter, Depends
from typing import List
from app.models.activity import RigViewActivity, PrimaveraActivity
from app.services.sync_service import get_primavera_activities

router = APIRouter()

@router.get("/sync/activities", response_model=List[RigViewActivity])
def sync_activities():
    # Chemi logica de business din services
    return get_primavera_activities()
