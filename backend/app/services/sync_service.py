from app.models.activity import PrimaveraActivity, RigViewActivity
from typing import List

def get_primavera_activities() -> List[RigViewActivity]:
    # Aici va fi conexiunea cu Primavera REST API sau SQL (momentan mock)
    activities = [
        PrimaveraActivity(
            activity_id="A1010", name="Land rental...", uwi="123", start="2024-07-01",
            finish="2024-07-05", status="Not Started", rig_view_code="S", project_status="Active"
        ),
        PrimaveraActivity(
            activity_id="A1200", name="Flowline execution", uwi="234", start="2024-08-01",
            finish="2024-08-05", status="Completed", rig_view_code="AR", project_status="Completed"
        ),
    ]
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
