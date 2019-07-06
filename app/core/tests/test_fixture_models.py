from django.test import TestCase
from core.models import FixtureManager


class FixtureModelTests(TestCase):

    def test_new_fixture_empty_name(self):
        """Test creating fixture with no name raises error"""
        with self.assertRaises(ValueError):
            FixtureManager.create_fixture(self, name=None, flat_id=1,
                                          price_value=5)

    def test_new_fixture_empty_flat(self):
        """Test creating fixture with no flat raises error"""
        with self.assertRaises(ValueError):
            FixtureManager.create_fixture(self, name='a', flat_id=None,
                                          price_value=300)

    def test_new_fixture_empty_pricevalue(self):
        """Test creating fixture with no price value raises error"""
        with self.assertRaises(ValueError):
            FixtureManager.create_fixture(self, name='a', flat_id=1,
                                          price_value=None)
