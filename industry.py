from typing import Optional, List
import requests

BASE_URL = "https://esi.evetech.net/latest"

def list_character_industry_jobs(token: str, character_id: int, page: Optional[int] = None):
    url = f"{BASE_URL}/characters/{character_id}/industry/jobs/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def character_mining_ledger(token: str, character_id: int, page: Optional[int] = None):
    url = f"{BASE_URL}/characters/{character_id}/mining/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def moon_extraction_timers(token: str, corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/mining/extractions/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def corporation_mining_observers(token: str, corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/mining/observers/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def observed_corporation_mining(token: str, corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/mining/observed/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def list_corporation_industry_jobs(token: str, corporation_id: int, page: Optional[int] = None):
    url = f"{BASE_URL}/corporations/{corporation_id}/industry/jobs/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def list_industry_facilities():
    url = f"{BASE_URL}/industry/facilities/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def list_solar_system_cost_indices():
    url = f"{BASE_URL}/industry/systems/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()
