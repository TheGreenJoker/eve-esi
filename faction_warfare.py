import requests

BASE_URL = "https://esi.evetech.net/latest"

def character_fw_stats(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/fw/stats"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def corporation_fw_stats(token: str, corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/fw/stats"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def fw_leaderboards():
    url = f"{BASE_URL}/fw/leaderboards"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def fw_leaderboards_characters():
    url = f"{BASE_URL}/fw/leaderboards/characters"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def fw_leaderboards_corporations():
    url = f"{BASE_URL}/fw/leaderboards/corporations"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def fw_stats():
    url = f"{BASE_URL}/fw/stats"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def fw_systems():
    url = f"{BASE_URL}/fw/systems"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def fw_wars():
    url = f"{BASE_URL}/fw/wars"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
