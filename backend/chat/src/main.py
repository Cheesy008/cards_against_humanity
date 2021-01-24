from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from .utils.service import notifier
from .utils.enums import WebsocketMessageType
from .config.settings import BACKEND_CORS_ORIGINS

app = FastAPI(title='Chat')

app.add_middleware(
    CORSMiddleware,
    allow_origins=BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    await notifier.generator.asend(None)


@app.websocket("/ws/{room_id}/{username}")
async def websocket_endpoint(websocket: WebSocket, room_id: int, username: str):
    message_common_data = dict(username=username, room_id=room_id)
    await notifier.connect(**message_common_data, websocket=websocket, message_type=WebsocketMessageType.USER_JOIN)
    try:
        while True:
            data = await websocket.receive_json()
            message_text = data.get('message_text', '')

            room_members = notifier.get_members(room_id) if notifier.get_members(room_id) is not None else []

            if websocket not in room_members:
                await notifier.connect(**message_common_data, websocket=websocket,
                                       message_type=WebsocketMessageType.USER_JOIN)

            await notifier.push(**message_common_data, message_text=message_text,
                                message_type=WebsocketMessageType.MESSAGE)
    except WebSocketDisconnect:
        await notifier.remove(**message_common_data, websocket=websocket, message_type=WebsocketMessageType.USER_LEAVE)

