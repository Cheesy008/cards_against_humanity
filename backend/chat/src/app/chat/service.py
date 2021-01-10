from typing import List

from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str, message_type: int):
        for connection in self.active_connections:
            await connection.send_json({'text': message, 'type': message_type})

    @staticmethod
    async def send_message(message: str, message_type: int, websocket: WebSocket):
        await websocket.send_json({'text': message, 'type': message_type})


manager = ConnectionManager()
