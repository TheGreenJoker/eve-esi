import requests

BASE_URL = "https://esi.evetech.net/latest"

def list_all_alliances():
    url = f"{BASE_URL}/alliances"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def alliance_info(alliance_id: int):
    url = f"{BASE_URL}/alliances/{alliance_id}"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def alliance_corporations(alliance_id: int):
    url = f"{BASE_URL}/alliances/{alliance_id}/corporations"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def alliance_icon(alliance_id: int):
    url = f"{BASE_URL}/alliances/{alliance_id}/icons"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
