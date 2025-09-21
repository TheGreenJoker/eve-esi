import requests
from typing import Optional

BASE_URL = "https://esi.evetech.net/latest"

def list_wars(max_war_id: Optional[int] = None, datasource: str = "tranquility"):
    url = f"{BASE_URL}/wars/"
    params = {}
    if max_war_id is not None: params["max_war_id"] = max_war_id
    params["datasource"] = datasource
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers, params=params).json()

def get_war_information(war_id: int, datasource: str = "tranquility"):
    url = f"{BASE_URL}/wars/{war_id}/"
    params = {"datasource": datasource}
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers, params=params).json()

def list_kills_for_a_war(war_id: int, page: Optional[int] = None, datasource: str = "tranquility"):
    url = f"{BASE_URL}/wars/{war_id}/killmails/"
    params = {"datasource": datasource}
    if page is not None: params["page"] = page
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers, params=params).json()
