import requests

BASE_URL = "https://esi.evetech.net/latest"

def get_character_recent_kills_and_losses(character_id: int, page: int = None):
    url = f"{BASE_URL}/characters/{character_id}/killmails/recent/"
    params = {"page": page} if page else None
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_corporation_recent_kills_and_losses(corporation_id: int, page: int = None):
    url = f"{BASE_URL}/corporations/{corporation_id}/killmails/recent/"
    params = {"page": page} if page else None
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_single_killmail(killmail_id: int, killmail_hash: str):
    url = f"{BASE_URL}/killmails/{killmail_id}/{killmail_hash}/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()