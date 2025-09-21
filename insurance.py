import requests

BASE_URL = "https://esi.evetech.net/latest"

def list_insurance_levels():
    url = f"{BASE_URL}/insurance/prices/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()
