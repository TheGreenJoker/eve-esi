import requests

BASE_URL = "https://esi.evetech.net/latest"

def character_clones(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/clones"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def character_active_implants(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/implants"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
