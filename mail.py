import requests

BASE_URL = "https://esi.evetech.net/latest"

def return_mail_headers(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/mail/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def send_new_mail(token: str, character_id: int, subject: str, body: str, recipients: list, recipient_type:str = "character"):
    url = f"{BASE_URL}/characters/{character_id}/mail/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json", "Content-Type": "application/json"}
    payload = {"subject": subject, "body": body, "recipients": [{"recipient_id": recipient, "recipient_type": recipient_type} for recipient in recipients]}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def get_mail_labels_and_unread_counts(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/mail/labels/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def create_mail_label(token: str, character_id: int, label_name: str):
    url = f"{BASE_URL}/characters/{character_id}/mail/labels/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json", "Content-Type": "application/json"}
    payload = {"name": label_name}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def delete_mail_label(token: str, character_id: int, label_id: int):
    url = f"{BASE_URL}/characters/{character_id}/mail/labels/{label_id}/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.delete(url, headers=headers)
    return response.status_code

def return_mailing_list_subscriptions(token: str, character_id: int):
    url = f"{BASE_URL}/characters/{character_id}/mail/lists/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def delete_mail(token: str, character_id: int, mail_id: int):
    url = f"{BASE_URL}/characters/{character_id}/mail/{mail_id}/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.delete(url, headers=headers)
    return response.status_code

def return_mail(token: str, character_id: int, mail_id: int):
    url = f"{BASE_URL}/characters/{character_id}/mail/{mail_id}/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def update_metadata_about_a_mail(token: str, character_id: int, mail_id: int, labels: list = None, read: bool = None):
    url = f"{BASE_URL}/characters/{character_id}/mail/{mail_id}/"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json", "Content-Type": "application/json"}
    payload = {}
    if labels is not None:
        payload["labels"] = labels
    if read is not None:
        payload["read"] = read
    response = requests.put(url, json=payload, headers=headers)
    return response.status_code
