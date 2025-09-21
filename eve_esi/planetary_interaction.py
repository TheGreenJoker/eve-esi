import requests

BASE_URL = "https://esi.evetech.net/latest"

def get_colonies(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/planets/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_colony_layout(token: str, character_id: int, planet_id: int):
    url = f"{BASE_URL}/characters/{character_id}/planets/{planet_id}/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def list_corporation_customs_offices(token: str, corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/customs_offices/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_schematic_information(schematic_id: int):
    url = f"{BASE_URL}/universe/schematics/{schematic_id}/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()
