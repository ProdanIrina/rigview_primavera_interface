from fastapi import APIRouter
from app.database import get_db_conn
from app.models.app_log import AppLog
from typing import List

router = APIRouter()

@router.get("/logs", response_model=List[AppLog])
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
