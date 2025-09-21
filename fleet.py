import requests

def get_character_fleet_info(token:int, character_id:int):
    url = f"https://esi.evetech.net/characters/{character_id}/fleet"

    headers = {
        "Accept-Language": "",
        "If-None-Match": "",
        "X-Compatibility-Date": "2020-01-01",
        "X-Tenant": "",
        "Accept": "application/json",
        "Authorization": token
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_fleet_information(token:int, fleet_id:int):
    url = f"https://esi.evetech.net/fleets/{fleet_id}"

    headers = {
        "Accept-Language": "",
        "If-None-Match": "",
        "X-Compatibility-Date": "2020-01-01",
        "X-Tenant": "",
        "Accept": "application/json",
        "Authorization": token
    }
    response = requests.get(url, headers=headers)
    return response.json()

def update_fleet(token:int, fleet_id:int, payload:dict):
    url = f"https://esi.evetech.net/fleets/{fleet_id}"

    headers = {
        "Accept-Language": "",
        "If-None-Match": "",
        "X-Compatibility-Date": "2020-01-01",
        "X-Tenant": "",
        "Accept": "application/json",
        "Authorization": token
    }
    response = requests.put(url, json=payload, headers=headers)
    return response.json()

def get_fleet_members(token:int, fleet_id:int):
    url = f"https://esi.evetech.net/fleets/{fleet_id}/members"

    headers = {
        "Accept-Language": "",
        "If-None-Match": "",
        "X-Compatibility-Date": "2020-01-01",
        "X-Tenant": "",
        "Accept": "application/json",
        "Authorization": token
    }
    response = requests.get(url, headers=headers)
    return response.json()

def create_fleet_invitation(
        token:int,
        fleet_id:int,
        payload = {
            "character_id": 0,
            "role": "fleet_commander",
            "squad_id": 0,
            "wing_id": 0
        }
    ):
    url = "https://esi.evetech.net/fleets/{fleet_id}/members"

    headers = {
        "Accept-Language": "",
        "If-None-Match": "",
        "X-Compatibility-Date": "2020-01-01",
        "X-Tenant": "",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": token
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def kick_fleet_members(token:int, fleet_id:int, member_id:int):
    url = f"https://esi.evetech.net/fleets/{fleet_id}/members/{member_id}"

    headers = {
        "Accept-Language": "",
        "If-None-Match": "",
        "X-Compatibility-Date": "2020-01-01",
        "X-Tenant": "",
        "Accept": "application/json",
        "Authorization": token
    }
    response = requests.delete(url, headers=headers)
    return response.json()

# Not finished

