from django.test import TestCase
from chatapp.models import Rooms, Chats


class RoomsTestCase(TestCase):
    def setUp(self):
        Rooms.objects.create(name="test_room")

    def test_room_name(self):
        room = Rooms.objects.get(name="test_room")
        self.assertEqual(room.name, "test_room")


class ChatsTestCase(TestCase):
    def setUp(self):
        room = Rooms.objects.create(name="test_room")
        Chats.objects.create(message="test_chat", room=room)

    def test_chat_message(self):
        chat = Chats.objects.get(message="test_chat")
        self.assertEqual(chat.message, "test_chat")
