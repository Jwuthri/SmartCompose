from fastapi import APIRouter

from smart_compose.api.api.routes import prediction
from smart_compose.api.api.routes import is_alive

api_router = APIRouter()
api_router.include_router(is_alive.router, tags=["health"], prefix="/health")
api_router.include_router(prediction.router, tags=["prediction"], prefix="/model")
