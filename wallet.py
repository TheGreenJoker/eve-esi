import requests
from typing import Optional

BASE_URL = "https://esi.evetech.net/latest"

def get_character_wallet_balance(token: str, character_id: int, datasource: str = "tranquility"):
    url = f"{BASE_URL}/characters/{character_id}/wallet/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    params = {"datasource": datasource}
    return requests.get(url, headers=headers, params=params).json()

def get_character_wallet_journal(token: str, character_id: int, page: Optional[int] = None, from_id: Optional[int] = None, datasource: str = "tranquility"):
    url = f"{BASE_URL}/characters/{character_id}/wallet/journal/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    params = {"datasource": datasource}
    if page is not None: params["page"] = page
    if from_id is not None: params["from_id"] = from_id
    return requests.get(url, headers=headers, params=params).json()

def get_character_wallet_transactions(token: str, character_id: int, page: Optional[int] = None, from_id: Optional[int] = None, datasource: str = "tranquility"):
    url = f"{BASE_URL}/characters/{character_id}/wallet/transactions/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    params = {"datasource": datasource}
    if page is not None: params["page"] = page
    if from_id is not None: params["from_id"] = from_id
    return requests.get(url, headers=headers, params=params).json()

def get_corporation_wallets(token: str, corporation_id: int, datasource: str = "tranquility"):
    url = f"{BASE_URL}/corporations/{corporation_id}/wallets/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    params = {"datasource": datasource}
    return requests.get(url, headers=headers, params=params).json()

def get_corporation_wallet_journal(token: str, corporation_id: int, division: int, page: Optional[int] = None, from_id: Optional[int] = None, datasource: str = "tranquility"):
    url = f"{BASE_URL}/corporations/{corporation_id}/wallets/{division}/journal/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    params = {"datasource": datasource}
    if page is not None: params["page"] = page
    if from_id is not None: params["from_id"] = from_id
    return requests.get(url, headers=headers, params=params).json()

def get_corporation_wallet_transactions(token: str, corporation_id: int, division: int, page: Optional[int] = None, from_id: Optional[int] = None, datasource: str = "tranquility"):
    url = f"{BASE_URL}/corporations/{corporation_id}/wallets/{division}/transactions/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    params = {"datasource": datasource}
    if page is not None: params["page"] = page
    if from_id is not None: params["from_id"] = from_id
    return requests.get(url, headers=headers, params=params).json()
