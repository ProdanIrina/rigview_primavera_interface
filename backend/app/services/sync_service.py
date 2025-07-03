from typing import List, Dict
from app.services.primavera_client import (
    get_projects,
    get_project_codes,
    get_activities,
    extract_uwi_from_codes,
    extract_rigview_code,
)
from app.models.activity import RigViewActivity  # trebuie să ai acest model (poate fi Pydantic)

def get_primavera_activities_for_sync() -> List[RigViewActivity]:
    """
    Returnează lista de activități din Primavera care trebuie sincronizate
    (doar proiecte active, doar activități cu RigView S/AR, doar dacă există UWI)
    """
    result = []
    projects = get_projects()
    for proj in projects:
        project_id = proj.get("ObjectId")
        codes = get_project_codes(project_id)
        uwi = extract_uwi_from_codes(codes)
        if not uwi:
            continue  # Sare proiectele fără UWI
        acts = get_activities(project_id)
        for act in acts:
            rigview_code = extract_rigview_code(act)
            if rigview_code not in ["S", "AR"]:
                continue
            # Construiți structura RigViewActivity (adaptează după modelul tău)
            result.append(
                RigViewActivity(
                    activity_id=act.get("Id"),
                    gate=act.get("Name"),
                    uwi=uwi,
                    start_date=act.get("StartDate"),
                    complete_date=act.get("FinishDate"),
                    status=act.get("Status"),
                    rig_view=rigview_code,
                )
            )
    return result
