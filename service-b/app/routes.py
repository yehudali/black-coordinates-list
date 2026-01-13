from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/coordinates", status_code=200)
async def save_data(data):
    status = 0 # save_cordinate(data)
    if not status:
        raise HTTPException(status_code=500, detail="Failed to save in db")
    return {"status":"saved!"}
   


@router.get("/coordinates")
async def get_all_data():
    redata = get_all_()
    return {"message": redata}