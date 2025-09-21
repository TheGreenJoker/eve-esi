import requests

BASE_URL = "https://esi.evetech.net/latest"

def calendar_event_summaries(token: str, character_id: int, from_event: str = None):
    url = f"{BASE_URL}/characters/{character_id}/calendar"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"from_event": from_event} if from_event else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def calendar_event_details(token: str, character_id: int, event_id: int):
    url = f"{BASE_URL}/characters/{character_id}/calendar/{event_id}"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def respond_calendar_event(token: str, character_id: int, event_id: int, response_value: str = "accepted"):
    url = f"{BASE_URL}/characters/{character_id}/calendar/{event_id}"
    headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    payload = {"response": response_value}
    response = requests.put(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def calendar_event_attendees(token: str, character_id: int, event_id: int):
    url = f"{BASE_URL}/characters/{character_id}/calendar/{event_id}/attendees"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
