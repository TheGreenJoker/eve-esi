import requests

BASE_URL = "https://esi.evetech.net/latest"

def get_character_attributes(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/attributes/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_character_skill_queue(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/skillqueue/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_character_skills(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/skills/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()
