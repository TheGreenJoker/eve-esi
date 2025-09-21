import requests

BASE_URL = "https://esi.evetech.net/latest"

def alliance_contacts(token: str, alliance_id: int, page: int = None):
    url = f"{BASE_URL}/alliances/{alliance_id}/contacts"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def alliance_contacts_labels(token: str, alliance_id: int):
    url = f"{BASE_URL}/alliances/{alliance_id}/contacts/labels"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def delete_contacts(token: str, character_id: int, contact_ids: list):
    url = f"{BASE_URL}/characters/{character_id}/contacts"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"contact_ids": contact_ids}
    response = requests.delete(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def character_contacts(token: str, character_id: int, page: int = None):
    url = f"{BASE_URL}/characters/{character_id}/contacts"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def add_contact(token: str, character_id: int, standing: float, label_ids: list, contact_ids: list):
    assert -10 <= standing <= 10, "standing must be in [-10,10]"
    url = f"{BASE_URL}/characters/{character_id}/contacts"
    headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    params = {"label_ids": label_ids, "standing": standing}
    response = requests.post(url, headers=headers, json=contact_ids, params=params)
    response.raise_for_status()
    return response.json()

def edit_contact(token: str, character_id: int, standing: float, label_ids: list, contact_ids: list):
    assert -10 <= standing <= 10, "standing must be in [-10,10]"
    url = f"{BASE_URL}/characters/{character_id}/contacts"
    headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    params = {"label_ids": label_ids, "standing": standing}
    response = requests.put(url, headers=headers, json=contact_ids, params=params)
    response.raise_for_status()
    return response.json()

def character_contacts_labels(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/contacts/labels"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def corporation_contacts(token: str, corporation_id: int, page: int = None):
    url = f"{BASE_URL}/corporations/{corporation_id}/contacts"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def corporation_contacts_labels(token: str, corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/contacts/labels"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
