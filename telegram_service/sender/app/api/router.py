from fastapi import APIRouter

from app.api.endpoints.routes import router

api_router = APIRouter()
api_router.include_router(router, tags=['tg'])