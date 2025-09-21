import requests

BASE_URL = "https://esi.evetech.net/latest"

def dogma_attributes():
    url = f"{BASE_URL}/dogma/attributes"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def dogma_attribute(attribute_id: int):
    url = f"{BASE_URL}/dogma/attributes/{attribute_id}"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def dogma_dynamic_item(type_id: int, item_id: int):
    url = f"{BASE_URL}/dogma/dynamic/items/{type_id}/{item_id}"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def dogma_effects():
    url = f"{BASE_URL}/dogma/effects"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def dogma_effect(effect_id: int):
    url = f"{BASE_URL}/dogma/effects/{effect_id}"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
