import requests

BASE_URL = "https://esi.evetech.net/latest"

# --- Character assets ---
def character_assets(token: str, character_id: int, page: int = None):
    url = f"{BASE_URL}/characters/{character_id}/assets"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def character_assets_locations(token: str, character_id: int, item_ids: list):
    url = f"{BASE_URL}/characters/{character_id}/assets/locations"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.post(url, headers=headers, json=item_ids)
    response.raise_for_status()
    return response.json()

def character_assets_names(token: str, character_id: int, item_ids: list):
    url = f"{BASE_URL}/characters/{character_id}/assets/names"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.post(url, headers=headers, json=item_ids)
    response.raise_for_status()
    return response.json()


# --- Corporation assets ---
def corporation_assets(token: str, corporation_id: int, page: int = None):
    url = f"{BASE_URL}/corporations/{corporation_id}/assets"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def corporation_assets_locations(token: str, corporation_id: int, item_ids: list):
    url = f"{BASE_URL}/corporations/{corporation_id}/assets/locations"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.post(url, headers=headers, json=item_ids)
    response.raise_for_status()
    return response.json()

def corporation_assets_names(token: str, corporation_id: int, item_ids: list):
    url = f"{BASE_URL}/corporations/{corporation_id}/assets/names"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.post(url, headers=headers, json=item_ids)
    response.raise_for_status()
    return response.json()
