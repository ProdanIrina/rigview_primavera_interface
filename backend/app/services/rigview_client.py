import requests

def send_activities_to_rigview(activities):
    """
    Trimite activitățile extrase din Primavera către API-ul RigView.
    Momentan, e doar mock. Când ai endpointul real, îl modifici aici.
    """
    # Exemplu de URL fals – înlocuiești cu cel real când îl primești!
    RIGVIEW_API_URL = "https://rigview.example.com/api/sync/activities"
    headers = {"Content-Type": "application/json"}

    # MOCK: doar afişează datele (fără POST real)
    print("Trimitem către RigView (mock):", activities)
    return {"success": True, "mock": True}

    # --- DĂ DRUMUL LA POST când ai endpointul lor:
    # resp = requests.post(RIGVIEW_API_URL, json=activities, headers=headers)
    # if resp.ok:
    #     return {"success": True, "response": resp.json()}
    # else:
    #     return {"success": False, "error": resp.text}
