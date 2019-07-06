from django.test import TestCase
from core.models import FlatManager


class FlatModelTests(TestCase):

    def test_new_flat_empty_name(self):
        """Test creating flat with no name raises error"""
        with self.assertRaises(ValueError):
            FlatManager.CreateFlat(self, name=None, buildingId=1)

    def test_new_flat_empty_building(self):
        """Test creating flat with no building raises error"""
        with self.assertRaises(ValueError):
            FlatManager.CreateFlat(self, name='a', buildingId=None)
