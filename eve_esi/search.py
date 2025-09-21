import requests

BASE_URL = "https://esi.evetech.net/latest"

def search_on_string(token: str, character_id: int, search: str, categories: list, strict: bool = False,
                     accept_language: str = "en", if_none_match: str = "", compatibility_date: str = "2020-01-01",
                     tenant: str = "tranquility"):
    url = f"{BASE_URL}/characters/{character_id}/search/"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Accept-Language": accept_language,
        "If-None-Match": if_none_match,
        "X-Compatibility-Date": compatibility_date,
        "X-Tenant": tenant
    }
    payload = {
        "search": search,
        "categories": categories,
        "strict": strict
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
