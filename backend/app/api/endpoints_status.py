from fastapi import APIRouter
from ..database import get_db_conn
from ..models.sync_status import SyncStatus

router = APIRouter()

@router.get("/status", response_model=list[SyncStatus])
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
