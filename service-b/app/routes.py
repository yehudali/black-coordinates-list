from fastapi import APIRouter, HTTPException
from storage import RedisDb
from schemas import CoordinatIp

router = APIRouter()
redis = RedisDb()

@router.post("/coordinates", status_code=200)
async def save_data(data : CoordinatIp):
    ip = data.ip
    body = data.model_dump_json()
    is_save = redis.set_data_to_db(ip, body)
    if not is_save:
        raise HTTPException(status_code=500, detail="Failed to save in db")
    return {"status":f"is_save{is_save}"}
   


@router.get("/coordinates")
async def get_all_data():
    try:
        redata = redis.get_all()
        return {"message": redata}
    except Exception as e:
        print(f"error{e}")
        return {"error" : str(e) }