import requests

BASE_URL = "https://esi.evetech.net/latest"

def list_incursions():
    url = f"{BASE_URL}/incursions/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()