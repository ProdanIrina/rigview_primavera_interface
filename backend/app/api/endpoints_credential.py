from fastapi import APIRouter
from app.utils.database import get_db_conn
from app.models.credential import Credential
from typing import List

router = APIRouter()

@router.get("/credentials", response_model=List[Credential])
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
