import requests

BASE_URL = "https://esi.evetech.net/latest"

def get_loyalty_points(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/loyalty/points/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def list_loyalty_store_offers(corporation_id: int):
    url = f"{BASE_URL}/loyalty/stores/{corporation_id}/offers/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()
