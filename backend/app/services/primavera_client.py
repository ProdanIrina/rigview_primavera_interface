from app.utils.config import PRIMAVERA_API_URL, PRIMAVERA_USER, PRIMAVERA_PASS
import requests

def get_auth():
    # Returnează tuple pentru Basic Auth
    return (PRIMAVERA_USER, PRIMAVERA_PASS)

def get_projects():
    """
    Ia toate proiectele ACTIVE din Primavera (Status != Completed/Canceled)
    """
    resp = requests.get(
        f"{PRIMAVERA_API_URL}/projects",
        auth=get_auth(),
        params={"fields": "ObjectId,Id,Name,Status"}
    )
    resp.raise_for_status()
    # Filtrare doar proiecte active
    return [p for p in resp.json().get("items", []) if p.get("Status") not in ["Completed", "Canceled"]]

def get_project_codes(project_id):
    """
    Ia codurile de proiect (inclusiv UWI) pentru un proiect dat.
    """
    resp = requests.get(
        f"{PRIMAVERA_API_URL}/projects/{project_id}/projectCodes",
        auth=get_auth()
    )
    resp.raise_for_status()
    return resp.json().get("items", [])

def get_activities(project_id):
    """
    Ia toate activitățile pentru un proiect dat.
    """
    resp = requests.get(
        f"{PRIMAVERA_API_URL}/projects/{project_id}/activities",
        auth=get_auth(),
        params={"fields": "ObjectId,Id,Name,StartDate,FinishDate,Status,ActivityCodeAssignments"}
    )
    resp.raise_for_status()
    return resp.json().get("items", [])

def extract_uwi_from_codes(codes):
    """
    Returnează codul UWI dacă există între codurile de proiect.
    """
    for c in codes:
        # Documentația Oracle: câmpul tipului e "ProjectCodeType"
        if c.get("ProjectCodeType") == "UWI":
            return c.get("ProjectCodeValue")
    return None

def extract_rigview_code(activity):
    """
    Din ActivityCodeAssignments, extrage codul de tip "Rig view"
    """
    for code in activity.get("ActivityCodeAssignments", []):
        if code.get("ActivityCodeType") == "Rig view":
            return code.get("ActivityCodeValue")
    return None
