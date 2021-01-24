from collections import defaultdict
from datetime import datetime
from fastapi import WebSocket
from fastapi.encoders import jsonable_encoder

from .enums import WebsocketMessageType


class Notifier:
    def __init__(self):
        self.connections: dict = defaultdict(dict)
        self.generator = self.get_notification_generator()

    async def get_notification_generator(self):
        while True:
            message = yield
            room_id = message.pop("room_id")
            await self._notify(message, room_id)

    def get_members(self, room_id):
        try:
            return self.connections[room_id]
        except Exception:
            return None

    async def push(self, message_text: str, username: str,
                   message_type: WebsocketMessageType, room_id: int):
        message_body = {
            "message_text": message_text,
            "date": jsonable_encoder(datetime.now()),
            "username": username,
            "room_id": room_id,
            "message_type": message_type
        }
        await self.generator.asend(message_body)

    async def connect(self, websocket: WebSocket, username: str,
                      message_type: WebsocketMessageType, room_id: int):
        await websocket.accept()
        if self.connections[room_id] == {} or len(self.connections[room_id]) == 0:
            self.connections[room_id] = []
        self.connections[room_id].append(websocket)

        message_body = {
            "message_text": f'Player {username} joined the game',
            "date": jsonable_encoder(datetime.now()),
            "room_id": room_id,
            "message_type": message_type
        }
        await self.generator.asend(message_body)

    async def remove(self, websocket: WebSocket, username: str,
                     message_type: WebsocketMessageType, room_id: int):
        self.connections[room_id].remove(websocket)
        # message_body = {
        #     "message_text": f'Player {username} left the game',
        #     "room_id": room_id,
        #     "message_type": message_type
        # }
        # await self.generator.asend(message_body)

    async def _notify(self, message: dict, room_id: int):
        living_connections = []
        while len(self.connections[room_id]) > 0:
            websocket = self.connections[room_id].pop()
            await websocket.send_json({'message': message})
            living_connections.append(websocket)
        self.connections[room_id] = living_connections


notifier = Notifier()
