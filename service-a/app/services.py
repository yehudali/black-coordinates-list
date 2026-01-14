import requests
from schemas import CoordinatIp
import os
def ip_to_json(ip:str):
    my_url = f"http://ip-api.com/json/{ip}"
    response = requests.get(my_url)
    return response.json()

def Clean_json(respons: dict):
    return CoordinatIp(
        ip = respons.get("query"),
        lat = respons.get("lat"),
        lon = respons.get("lon")
        )

def connecting_servers(data:CoordinatIp):
    url = os.getenv("SERVICE_B_URL", "http://127.0.0.1:8001")
    service_b = f"{url}/coordinates"
    response = requests.post(service_b, json=data.model_dump())
    return response.status_code