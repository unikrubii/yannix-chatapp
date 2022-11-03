from datetime import datetime
from ninja import Schema


class RoomIn(Schema):
    message: str
    room_id: int


class RoomOut(Schema):
    id: int
    name: str
    chats: list[str]


class ErrorOut(Schema):
    message: str


class ChatOut(Schema):
    id: int
    message: str
    room_name: str
    timestamp: datetime
