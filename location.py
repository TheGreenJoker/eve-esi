import requests

BASE_URL = "https://esi.evetech.net/latest"

def get_character_location(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/location/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_character_online(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/online/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_current_ship(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/ship/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()
