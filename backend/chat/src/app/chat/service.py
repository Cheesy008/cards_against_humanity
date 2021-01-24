from collections import defaultdict
from typing import List, Dict

from fastapi import WebSocket


class Notifier:
    def __init__(self):
        self.connections: dict = defaultdict(dict)
        self.generator = self.get_notification_generator()

    async def get_notification_generator(self):
        while True:
            message = yield
            print(f"MESSAGE : {message}")
            msg = message["message"]
            room_id = message["room_id"]
            await self._notify(msg, room_id)

    def get_members(self, room_id):
        try:
            return self.connections[room_id]
        except Exception:
            return None

    async def push(self, msg: str, room_id: int):
        message_body = {"message": msg, "room_id": room_id}
        await self.generator.asend(message_body)

    async def connect(self, websocket: WebSocket, room_id: int):
        await websocket.accept()
        if self.connections[room_id] == {} or len(self.connections[room_id]) == 0:
            self.connections[room_id] = []
        self.connections[room_id].append(websocket)
        print(f"CONNECTIONS : {self.connections[room_id]}")

    def remove(self, websocket: WebSocket, room_id: int):
        self.connections[room_id].remove(websocket)

    async def _notify(self, message: str, room_id: int):
        living_connections = []
        while len(self.connections[room_id]) > 0:
            # Looping like this is necessary in case a disconnection is handled
            # during await websocket.send_text(message)
            websocket = self.connections[room_id].pop()
            await websocket.send_json({'text': message})
            living_connections.append(websocket)
        self.connections[room_id] = living_connections


notifier = Notifier()
