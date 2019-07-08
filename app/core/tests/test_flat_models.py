# from django.contrib.auth import get_user_model

from django.test import TestCase
from core.models import Flat


class FlatModelTests(TestCase):

    def test_new_flat_empty_name(self):
        """Test creating flat with no name raises error"""
        with self.assertRaises(ValueError):
            Flat.objects.create_flat(name=None, building=1)

    def test_new_flat_empty_user(self):
        """Test creating flat with no name raises error"""
        with self.assertRaises(ValueError):
            Flat.objects.create_flat(name='acb', user=None, building=1)

    def test_new_flat_empty_building(self):
        """Test creating flat with no building raises error"""
        with self.assertRaises(ValueError):
            Flat.objects.create_flat(name='a', building=None)
