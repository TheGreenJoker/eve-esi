import requests

BASE_URL = "https://esi.evetech.net/latest"

def npc_corporations():
    url = f"{BASE_URL}/corporations/npccorps"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def corporation_info(corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def corporation_alliance_history(corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/alliancehistory"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def corporation_blueprints(token: str, corporation_id: int, page: int = None):
    url = f"{BASE_URL}/corporations/{corporation_id}/blueprints"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def corporation_alsc_logs(token: str, corporation_id: int, page: int = None):
    url = f"{BASE_URL}/corporations/{corporation_id}/containers/logs"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def corporation_divisions(token: str, corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/divisions"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def corporation_facilities(token: str, corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/facilities"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def corporation_icon(corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/icons"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def corporation_medals(token: str, corporation_id: int, page: int = None):
    url = f"{BASE_URL}/corporations/{corporation_id}/medals"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def corporation_issued_medals(token: str, corporation_id: int, page: int = None):
    url = f"{BASE_URL}/corporations/{corporation_id}/medals/issued"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def corporation_members(corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/members"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def corporation_member_limit(corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/members/limit"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def corporation_member_titles(token: str, corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/members/titles"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def corporation_member_tracking(token: str, corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/membertracking"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def corporation_member_roles(token: str, corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/members/roles"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def corporation_member_roles_history(token: str, corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/members/roles/history"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def corporation_shareholders(token: str, corporation_id: int, page: int = None):
    url = f"{BASE_URL}/corporations/{corporation_id}/shareholders"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def corporation_standings(token: str, corporation_id: int, page: int = None):
    url = f"{BASE_URL}/corporations/{corporation_id}/standings"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def corporation_starbases(token: str, corporation_id: int, page: int = None):
    url = f"{BASE_URL}/corporations/{corporation_id}/starbases"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def starbase_detail(token: str, corporation_id: int, system_id: int, page: int = None):
    url = f"{BASE_URL}/corporations/{corporation_id}/starbases/{system_id}"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def corporation_structures(token: str, corporation_id: int, page: int = None):
    url = f"{BASE_URL}/corporations/{corporation_id}/structures"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    params = {"page": page} if page else None
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def corporation_titles(token: str, corporation_id: int):
    url = f"{BASE_URL}/corporations/{corporation_id}/titles"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
