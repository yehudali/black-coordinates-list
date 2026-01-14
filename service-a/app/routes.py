from fastapi import APIRouter
import services
from schemas import CoordinatIp

router = APIRouter()


@router.post("/")
def post(input1:CoordinatIp):
    respons = services.ip_to_json(input1.ip)
    json_to_send = services.Clean_json(respons)
    status = services.connectinga_servers(json_to_send)
    return json_to_send




#דוגמה
# {"213.151.56.89":{"lat":31.7674,"lon":35.2186}}