import requests

BASE_URL = "https://esi.evetech.net/latest"

def character_contracts(token: str, character_id: int, page: int = None):
    url = f"{BASE_URL}/characters/{character_id}/contracts"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def character_contract_bids(token: str, character_id: int, contract_id: int):
    url = f"{BASE_URL}/characters/{character_id}/contracts/{contract_id}/bids"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def character_contract_items(token: str, character_id: int, contract_id: int):
    url = f"{BASE_URL}/characters/{character_id}/contracts/{contract_id}/items"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def public_contract_bids(contract_id: int, page: int = None):
    url = f"{BASE_URL}/characters/public/contracts/{contract_id}/bids"
    headers = {"Accept": "application/json"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def public_contract_items(contract_id: int, page: int = None):
    url = f"{BASE_URL}/characters/public/contracts/{contract_id}/items"
    headers = {"Accept": "application/json"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def public_contracts(region_id: int, page: int = None):
    url = f"{BASE_URL}/characters/public/{region_id}"
    headers = {"Accept": "application/json"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def corporation_contracts(token: str, corporation_id: int, page: int = None):
    url = f"{BASE_URL}/corporations/{corporation_id}/contracts"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def corporation_contract_bids(token: str, corporation_id: int, contract_id: int, page: int = None):
    url = f"{BASE_URL}/corporations/{corporation_id}/contracts/{contract_id}/bids"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def corporation_contract_items(token: str, corporation_id: int, contract_id: int, page: int = None):
    url = f"{BASE_URL}/corporations/{corporation_id}/contracts/{contract_id}/items"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()
