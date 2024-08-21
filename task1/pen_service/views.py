import aioredis
from fastapi import APIRouter
from fastapi import Request, Query

from .services import service_write_data, get_check_data


router = APIRouter()


@router.post("/write_data")
async def write_data(request: Request):
    data = await request.json()
    return await service_write_data(data)


@router.get("/check_data")
async def check_data(phone: str  = Query(pattern=r"^\d{11}$")):
    return await get_check_data(phone)
