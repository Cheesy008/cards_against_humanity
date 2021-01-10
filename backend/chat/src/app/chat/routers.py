from fastapi import APIRouter

from . import endpoint

api_router = APIRouter()

api_router.include_router(endpoint.websocket_router, prefix='/chat')
