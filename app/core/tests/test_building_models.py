from django.test import TestCase
from core.models import Building


class BuildingModelTests(TestCase):

    def test_new_building_empty_name(self):
        """Test creating building with no name raises error"""
        with self.assertRaises(ValueError):
            Building.objects.create_building(name=None)
