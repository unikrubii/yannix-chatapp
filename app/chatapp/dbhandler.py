from chatapp.models import Rooms, Chats


class DBHandler:
    def __init__(self, request):
        self.request = request

    def get_all_rooms(self):
        """
            It gets all the rooms from the database and returns them in a list.
        """
        response = []
        rooms = Rooms.objects.all()
        for room in rooms:
            chats = Chats.objects.all().filter(room_id=room.id)
            response.append({
                    "id": room.id,
                    "name": room.name,
                    "chats": [chat.message for chat in chats],
                })

        return response

    def get_room_by_id(self, room_id):
        """
            It gets a room by its id.
        """
        try:
            room = Rooms.objects.get(id=room_id)
        except Rooms.DoesNotExist:
            print("test")
            return None
        chats = Chats.objects.all().filter(room_id=room.id)
        return {
            "id": room.id,
            "name": room.name,
            "chats": [chat.message for chat in chats],
        }

    def get_room_chats(self, room_id):
        """
            It gets all the chats in a room.
        """

        chats = Chats.objects.all().filter(room_id=room_id)
        response = []
        for chat in chats:
            response.append({
                "id": chat.id,
                "message": chat.message,
                "room_name": chat.room.name,
                "timestamp": chat.timestamp,
            })
        return response

    def get_chat_by_id(self, chat_id):
        """
            This function returns a chat object given a chat id.
        """
        try:
            chat = Chats.objects.get(id=chat_id)
        except Chats.DoesNotExist:
            return None
        return {
            "id": chat.id,
            "message": chat.message,
            "room_name": chat.room.name,
            "timestamp": chat.timestamp,
        }

    def create_room(self, name):
        """
            This function creates a room given a name.
        """
        if name in [room.name for room in Rooms.objects.all()]:
            return None
        room = Rooms.objects.create(name=name)
        return {
            "id": room.id,
            "name": room.name,
            "chats": [],
        }

    def add_chat(self, room_id, message):
        """
            This function adds a chat to a room.
        """
        try:
            room = Rooms.objects.get(id=room_id)
        except Rooms.DoesNotExist:
            return None
        chat = Chats.objects.create(room=room, message=message)
        return {
            "id": chat.id,
            "message": chat.message,
            "room_name": chat.room.name,
            "timestamp": chat.timestamp,
        }

    def delete_room(self, room_id):
        """
            This function deletes a room given a room id.
        """
        try:
            room = Rooms.objects.get(id=room_id)
        except Rooms.DoesNotExist:
            return None
        room_name = room.name
        room.delete()
        return f'Room {room_id} ({room_name}) deleted.'
