from fastapi import APIRouter
from typing import List
from app.models.activity import RigViewActivity
from app.services.sync_service import get_sync_activities

router = APIRouter()

@router.get("/sync/activities", response_model=List[RigViewActivity])
def sync_activities():
    return get_sync_activities()
