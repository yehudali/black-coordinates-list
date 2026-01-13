import requests
from schemas import CoordinatIp

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
    servise_b = f"http://localhost:8001/coordinates"
    response = requests.post(servise_b, json=data.model_dump())
    return response.status_code