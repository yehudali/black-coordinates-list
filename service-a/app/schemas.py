from typing import Optional
from pydantic import BaseModel


class CoordinatIp(BaseModel):
    ip: str
    lat: Optional[float]
    lon: Optional[float]