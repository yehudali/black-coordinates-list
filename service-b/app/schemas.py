from pydantic import BaseModel


class CoordinatIp(BaseModel):
    ip: str 
    lat: float
    lon: float

