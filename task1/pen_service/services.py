import re

from fastapi.responses import JSONResponse

from .db import client_redis


async def service_write_data(data):
    if "phone" not in data or "address" not in data:
        return JSONResponse(status_code=400, content={"error": "Нет нужных полей"})

    phone = data["phone"]
    address = data["address"]

    pattern = r"^\d{11}$"

    if not re.match(pattern, phone):
        return JSONResponse(status_code=400, content={"error": "Неправильный формат телефона"})

    user_data = await client_redis.get(f'{phone}')

    await client_redis.set(f'{phone}', f'{address}')

    if user_data is None:
        return JSONResponse(status_code=201, content={"message": f"Данные успешно добавлены"})

    return JSONResponse(status_code=200, content={"message": f"Данные '{user_data.decode()}' успешно изменены"})


async def get_check_data(phone: str):
    user_data = await client_redis.get(f'{phone}')

    if user_data is None:
        return JSONResponse(status_code=200, content={"message": f"Таких данных нет"})

    return JSONResponse(status_code=200, content={"message": f"{user_data.decode()}"})
