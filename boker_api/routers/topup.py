from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_topup():
    return {"Hello": "topup"}
