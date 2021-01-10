from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, APIRouter

from .service import manager

websocket_router = APIRouter()


@websocket_router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket)
    await manager.broadcast(f"Игрок {username} вошёл в игру")
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Игрок {username} вышел из игры")

