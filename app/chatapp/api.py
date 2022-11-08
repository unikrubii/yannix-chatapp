from ninja import Router
from chatapp.dbhandler import DBHandler
from chatapp.serializer import (
    RoomIn,
    RoomOut,
    ErrorOut,
    ChatOut,
)


router = Router()


@router.get("/rooms", response={200: list[RoomOut]})
def get_all_rooms(request):
    """
        Returning a list of all the rooms in the database.
    """

    command = DBHandler(request)
    response = command.get_all_rooms()

    return response


@router.get("/rooms/{room_id}/", response={200: RoomOut, 404: ErrorOut})
def get_room_by_id(request, room_id: int):
    """
        A function that takes in room_id and returns a response.
    """
    # print(room_id)
    command = DBHandler(request)
    response = command.get_room_by_id(room_id)
    # print(response)
    # return None

    if not response:
        return 404, {"message": f"No room with id: {room_id}"}
    return 200, response


@router.get("/chats/room/{room_id}/", response={200: list[ChatOut], 404: ErrorOut})
def get_room_chats(request, room_id: int):
    """
        A function that takes in room_id and returns a list of chats.
    """
    command = DBHandler(request)
    response = command.get_room_chats(room_id)

    if not response:
        return 404, {"message": f"No chat in room id: {room_id}"}
    return 200, response


@router.get("/chats/{chat_id}/", response={200: ChatOut, 404: ErrorOut})
def get_chat_by_id(request, chat_id: int):
    """
        A function that takes in chat_id and returns a chat.
    """
    command = DBHandler(request)
    response = command.get_chat_by_id(chat_id)

    if response is None:
        return 404, {"message": f"No chat with id: {chat_id}"}
    return 200, response


@router.post("/rooms/", response={201: RoomOut, 400: ErrorOut})
def create_room(request, name: str):
    """
        A function that takes in room_name and returns a response.
    """
    command = DBHandler(request)
    response = command.create_room(name)
    if response is None:
        return 400, {"message": f"Room with name: {name} already exists"}
    return 201, response


@router.post("/chats/", response={201: ChatOut, 404: ErrorOut})
def add_chat(request, RoomIn: RoomIn):
    """
        A function that takes in room_id and message and returns a response.
    """
    command = DBHandler(request)
    response = command.add_chat(RoomIn.room_id, RoomIn.message)

    if response is None:
        return 404, {"message": f"No room with id: {RoomIn.room_id}"}
    return 201, response


@router.delete("/rooms/{room_id}", response={200: str, 404: ErrorOut})
def delete_room(request, room_id: int):
    """
        A function that takes in room_id and returns a response.
    """
    command = DBHandler(request)
    response = command.delete_room(room_id)

    if response is None:
        return 404, {"message": f"No room with id: {room_id}"}
    return 200, response
