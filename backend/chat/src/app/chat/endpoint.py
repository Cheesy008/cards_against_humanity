import json
from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, APIRouter

from .service import notifier

websocket_router = APIRouter()


@websocket_router.on_event("startup")
async def startup_event():
    await notifier.generator.asend(None)


@websocket_router.websocket("/ws/{room_id}/{username}")
async def websocket_endpoint(websocket: WebSocket, room_id: int, username: str):
    await notifier.connect(websocket, room_id)
    try:
        while True:
            d = await websocket.receive_json()
            d["room_id"] = room_id
            print(f"UPDATING DB with: {d}")

            room_members = notifier.get_members(room_id) if notifier.get_members(room_id) is not None else []
            if websocket not in room_members:
                print("SENDER NOT IN ROOM MEMBERS: RECONNECTING")
                await notifier.connect(websocket, room_id)

            await notifier.push(f"{d}", room_id)
    except WebSocketDisconnect:
        notifier.remove(websocket, room_id)
