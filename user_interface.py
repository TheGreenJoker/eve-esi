import requests
from typing import List, Optional

BASE_URL = "https://esi.evetech.net/latest"

def set_autopilot_waypoint(token: str, destination_id: int, add_to_beginning: bool = False, clear_other_waypoints: bool = False, datasource: str = "tranquility"):
    url = f"{BASE_URL}/ui/autopilot/waypoint/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    params = {"destination_id": destination_id, "add_to_beginning": str(add_to_beginning).lower(), "clear_other_waypoints": str(clear_other_waypoints).lower(), "datasource": datasource}
    return requests.post(url, headers=headers, params=params).status_code

def open_contract_window(token: str, contract_id: int):
    url = f"{BASE_URL}/ui/openwindow/contract/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json", "Content-Type": "application/json"}
    payload = {"contract_id": contract_id}
    return requests.post(url, headers=headers, json=payload).status_code

def open_information_window(token: str, target_id: int):
    url = f"{BASE_URL}/ui/openwindow/information/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json", "Content-Type": "application/json"}
    payload = {"id": target_id}
    return requests.post(url, headers=headers, json=payload).status_code

def open_market_details(token: str, type_id: int):
    url = f"{BASE_URL}/ui/openwindow/marketdetails/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json", "Content-Type": "application/json"}
    payload = {"type_id": type_id}
    return requests.post(url, headers=headers, json=payload).status_code

def open_new_mail_window(token: str, subject: Optional[str] = None, body: Optional[str] = None, recipients: Optional[List[int]] = None, to_corp_or_alliance_id: Optional[int] = None, to_mailing_list_id: Optional[int] = None):
    url = f"{BASE_URL}/ui/openwindow/newmail/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json", "Content-Type": "application/json"}
    payload = {}
    if subject is not None: payload["subject"] = subject
    if body is not None: payload["body"] = body
    if recipients is not None: payload["recipients"] = recipients
    if to_corp_or_alliance_id is not None: payload["to_corp_or_alliance_id"] = to_corp_or_alliance_id
    if to_mailing_list_id is not None: payload["to_mailing_list_id"] = to_mailing_list_id
    return requests.post(url, headers=headers, json=payload).status_code
