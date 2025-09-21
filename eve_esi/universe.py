from typing import Optional, List
import requests

BASE_URL = "https://esi.evetech.net/latest"

def ancestries():
    url = f"{BASE_URL}/universe/ancestries/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def asteroid_belt_information(belt_id: int):
    url = f"{BASE_URL}/universe/asteroid_belts/{belt_id}/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def bloodlines():
    url = f"{BASE_URL}/universe/bloodlines/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def item_categories():
    url = f"{BASE_URL}/universe/categories/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def item_category_information(category_id: int):
    url = f"{BASE_URL}/universe/categories/{category_id}/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def constellations():
    url = f"{BASE_URL}/universe/constellations/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def constellation_information(constellation_id: int):
    url = f"{BASE_URL}/universe/constellations/{constellation_id}/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def factions():
    url = f"{BASE_URL}/universe/factions/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def graphics():
    url = f"{BASE_URL}/universe/graphics/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def graphic_information(graphic_id: int):
    url = f"{BASE_URL}/universe/graphics/{graphic_id}/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def item_groups(page: int = None):
    url = f"{BASE_URL}/universe/groups/"
    headers = {"Accept": "application/json"}
    params = {"page": page} if page else None
    return requests.get(url, headers=headers, params=params).json()

def item_group_information(group_id: int):
    url = f"{BASE_URL}/universe/groups/{group_id}/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def bulk_names_to_ids(names: list):
    url = "https://esi.evetech.net/universe/ids"
    headers = {"Accept-Language": "","If-None-Match": "","X-Compatibility-Date": "2025-08-26","X-Tenant": "","Content-Type": "application/json","Accept": "application/json"}
    return requests.post(url, json=names, headers=headers).json()

def moon_information(moon_id: int):
    url = f"{BASE_URL}/universe/moons/{moon_id}/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def names_and_categories(ids: list):
    url = f"{BASE_URL}/universe/names/"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    return requests.post(url, headers=headers, json=ids).json()

def planet_information(planet_id: int, language: str = "en"):
    url = f"{BASE_URL}/universe/planets/{planet_id}/"
    headers = {"Accept": "application/json", "Accept-Language": language}
    return requests.get(url, headers=headers).json()

def character_races():
    url = f"{BASE_URL}/universe/races/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def regions():
    url = f"{BASE_URL}/universe/regions/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def region_information(region_id: int, language: str = "en"):
    url = f"{BASE_URL}/universe/regions/{region_id}/"
    headers = {"Accept": "application/json", "Accept-Language": language}
    return requests.get(url, headers=headers).json()

def stargate_information(stargate_id: int):
    url = f"{BASE_URL}/universe/stargates/{stargate_id}/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def star_information(star_id: int):
    url = f"{BASE_URL}/universe/stars/{star_id}/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def station_information(station_id: int, language: str = "en"):
    url = f"{BASE_URL}/universe/stations/{station_id}/"
    headers = {"Accept": "application/json", "Accept-Language": language}
    return requests.get(url, headers=headers).json()

def list_all_public_structures():
    url = f"{BASE_URL}/universe/structures/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def structure_information(structure_id: int, token: Optional[str] = None):
    url = f"{BASE_URL}/universe/structures/{structure_id}/"
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return requests.get(url, headers=headers).json()

def system_jumps():
    url = f"{BASE_URL}/universe/system_jumps/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def system_kills():
    url = f"{BASE_URL}/universe/system_kills/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def solar_systems():
    url = f"{BASE_URL}/universe/systems/"
    headers = {"Accept": "application/json"}
    return requests.get(url, headers=headers).json()

def solar_system_information(system_id: int, language: str = "en"):
    url = f"{BASE_URL}/universe/systems/{system_id}/"
    headers = {"Accept": "application/json", "Accept-Language": language}
    return requests.get(url, headers=headers).json()

def types(page: Optional[int] = None):
    url = f"{BASE_URL}/universe/types/"
    headers = {"Accept": "application/json"}
    params = {"page": page} if page is not None else None
    return requests.get(url, headers=headers, params=params).json()

def type_information(type_id: int, language: str = "en"):
    url = f"{BASE_URL}/universe/types/{type_id}/"
    headers = {"Accept": "application/json", "Accept-Language": language}
    return requests.get(url, headers=headers).json()
