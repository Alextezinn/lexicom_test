from fastapi import APIRouter

from pen_service import views


routes = APIRouter()

routes.include_router(views.router)
