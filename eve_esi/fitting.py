import requests

BASE_URL = "https://esi.evetech.net/latest"

def get_fittings(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/fittings"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def create_fitting(token: str, character_id: int, fit: dict):
    url = f"{BASE_URL}/characters/{character_id}/fittings"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.post(url, json=fit, headers=headers)
    response.raise_for_status()
    return response.json()

def delete_fitting(token: str, character_id: int, fitting_id: int):
    url = f"{BASE_URL}/characters/{character_id}/fittings/{fitting_id}"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    return response.json()
