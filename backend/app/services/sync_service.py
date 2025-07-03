from typing import List, Dict
from app.services.primavera_client import (
    get_projects,
    get_project_codes,
    get_activities,
    extract_uwi_from_codes,
    extract_rigview_code,
)
from app.models.activity import RigViewActivity  # trebuie să ai acest model (poate fi Pydantic)

def get_sync_activities() -> List[RigViewActivity]:
    projects = get_projects()
    result = []
    for proj in projects:
        codes = get_project_codes(proj["ObjectId"])
        uwi = extract_uwi_from_codes(codes)
        if not uwi:
            continue
        acts = get_activities(proj["ObjectId"])
        for act in acts:
            rigview_code = extract_rigview_code(act)
            if rigview_code not in ["S", "AR"]:
                continue
            result.append(RigViewActivity(
                activity_id=act["Id"],
                gate=act["Name"],
                uwi=uwi,
                start_date=act.get("StartDate"),
                complete_date=act.get("FinishDate"),
                status=act.get("Status"),
                rig_view=rigview_code
            ))
    return result
