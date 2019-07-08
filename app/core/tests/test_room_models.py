# from django.contrib.auth import get_user_model

from django.test import TestCase
from core.models import Room


class RoomModelTests(TestCase):

    def test_new_room_empty_name(self):
        """Test creating room with no name raises error"""
        with self.assertRaises(ValueError):
            Room.objects.create_room(
                name=None, user=1, flat=1
            )

    def test_new_room_empty_user(self):
        """Test creating room with no user raises error"""
        with self.assertRaises(ValueError):
            Room.objects.create_room(
                name=1, user=None, flat=1
            )

    def test_new_room_empty_room(self):
        """Test creating room with no flat raises error"""
        with self.assertRaises(ValueError):
            Room.objects.create_room(
                name='a', user=4, flat=None
            )
