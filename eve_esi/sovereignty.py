import requests

BASE_URL = "https://esi.evetech.net/latest"

def list_sovereignty_campaigns():
    url = f"{BASE_URL}/sovereignty/campaigns/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def list_sovereignty_of_systems():
    url = f"{BASE_URL}/sovereignty/map/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def list_sovereignty_structures():
    url = f"{BASE_URL}/sovereignty/structures/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()
