import requests

BASE_URL = "https://esi.evetech.net/latest"

def get_route(from_system_id: int, to_system_id: int, flag: str = "shortest", avoid_solar_system_ids: list = None):
    url = f"{BASE_URL}/route/{from_system_id}/{to_system_id}/"
    params = {"flag": flag}
    if avoid_solar_system_ids:
        params["avoid"] = ",".join(map(str, avoid_solar_system_ids))
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers, params=params)
    return response.json()
