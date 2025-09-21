import requests

BASE_URL = "https://esi.evetech.net/latest"

def list_open_orders_from_character(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/orders/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def list_historical_orders_by_character(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/orders/history/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def list_open_orders_from_corporation(token: str, corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/orders/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def list_historical_orders_from_corporation(token: str, corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/orders/history/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_item_groups():
    url = f"{BASE_URL}/universe/groups/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_item_group_information(group_id: int):
    url = f"{BASE_URL}/universe/groups/{group_id}/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def list_market_prices():
    url = f"{BASE_URL}/markets/prices/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def list_orders_in_structure(structure_id: int):
    url = f"{BASE_URL}/markets/structures/{structure_id}/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def list_historical_market_statistics_in_region(region_id: int):
    url = f"{BASE_URL}/markets/{region_id}/history/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def list_orders_in_region(region_id: int):
    url = f"{BASE_URL}/markets/{region_id}/orders/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def list_type_ids_relevant_to_market(market_group_id: int):
    url = f"{BASE_URL}/markets/groups/{market_group_id}/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()
