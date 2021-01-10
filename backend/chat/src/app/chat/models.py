from typing import Optional, List

from pydantic import BaseModel, Field


class Message(BaseModel):
    user_id: int = Field(...)
    username: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "user_id": 1,
                "username": "cheesy",
                "content": "lalala"
            }
        }


class Room(BaseModel):
    room_id: int = Field(...)
    messages: Optional[List[Message]] = []

    class Config:
        schema_extra = {
            "example": {
                "room_id": 1,
                "messages": [
                    {
                        "user_id": 1,
                        "username": "cheesy",
                        "content": "lalala"
                    },
                    {
                        "user_id": 2,
                        "username": "user2",
                        "content": "hi"
                    }
                ]
            }
        }
