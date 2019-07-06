from django.test import TestCase
from core.models import BuildingManager


class BuildingModelTests(TestCase):

    def test_new_building_empty_name(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            BuildingManager.CreateBuilding(None)
