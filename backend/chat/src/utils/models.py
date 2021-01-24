from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class Message(BaseModel):
    user_id: Optional[int] = None
    username: Optional[str] = None
    message_text: str
    message_type: str
    date: datetime

    class Config:
        schema_extra = {
            "example": {
                "user_id": 1,
                "username": "cheesy",
                "message_text": "lalala",
                "message_type": 1,
                "date": "2021-01-24 22:51:17.606046"
            }
        }


class Room(BaseModel):
    room_id: int
    messages: Optional[List[Message]] = []

    class Config:
        schema_extra = {
            "example": {
                "room_id": 1,
                "messages": [
                    {
                        "user_id": 1,
                        "username": "cheesy",
                        "message_text": "lalala",
                        "message_type": 1,
                        "date": "2021-01-24 22:51:17.606046"
                    },
                    {
                        "user_id": None,
                        "username": None,
                        "message_text": "Player cheesy joined the game",
                        "message_type": 2,
                        "date": "2021-01-24 22:51:17.606046"
                    }
                ]
            }
        }
