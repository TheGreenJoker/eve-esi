import requests

BASE_URL = "https://esi.evetech.net/latest"

def get_server_status():
    url = f"{BASE_URL}/status/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()
