# from django.contrib.auth import get_user_model

from django.test import TestCase
from core.models import Building


class BuildingModelTests(TestCase):

    def test_new_building_empty_name(self):
        """Test creating building with no name raises error"""
        with self.assertRaises(ValueError):
            Building.objects.create_building(name=None, user=1)

    def test_new_building_empty_user(self):
        """Test creating building with no user raises error"""
        with self.assertRaises(ValueError):
            Building.objects.create_building(name='adda', user=None)
