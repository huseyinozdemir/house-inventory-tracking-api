from django.test import TestCase
from core.models import Flat, Building


def sample_building(name="A2"):
    """Create a sample building"""
    return Building.objects.create_building(name)


class FlatModelTests(TestCase):

    def test_new_flat_empty_name(self):
        """Test creating flat with no name raises error"""
        with self.assertRaises(ValueError):
            Flat.objects.create_flat(name=None, building_id=1)

    def test_new_flat_empty_building(self):
        """Test creating flat with no building raises error"""
        with self.assertRaises(ValueError):
            Flat.objects.create_flat(name='a', building_id=None)

    def test_flat_str(self):
        """Test the flat string representation"""
        flat = Flat.objects.create_flat(
            name='D1',
            building_id=sample_building()
        )

        self.assertEqual(str(flat), flat.name)
