import requests

BASE_URL = "https://esi.evetech.net/latest"

def characters_affiliations(characters_id: list):
    url = f"{BASE_URL}/characters/affiliation"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    response = requests.post(url, json=characters_id, headers=headers)
    response.raise_for_status()
    return response.json()

def character_public_info(character_id: int):
    url = f"{BASE_URL}/characters/{character_id}"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def character_agents_research(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/agents_research"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def character_blueprints(token: str, character_id: int, page: int = None):
    url = f"{BASE_URL}/characters/{character_id}/blueprints"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def character_corporation_history(character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/corporationhistory"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def character_cspa_cost(token: str, character_id: int, characters_id: list):
    url = f"{BASE_URL}/characters/{character_id}/cspa"
    headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.post(url, json=characters_id, headers=headers)
    response.raise_for_status()
    return response.json()

def character_jump_fatigue(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/fatigue"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def character_medals(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/medals"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def character_notifications(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/notifications"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def character_new_contact_notifications(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/notifications/contacts"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def character_portrait(character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/portrait"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def character_standings(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/standings"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def character_corporation_titles(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/titles"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
