from django.test import TestCase
from core.models import FixtureManager


class FixtureModelTests(TestCase):

    def test_new_fixture_empty_name(self):
        """Test creating fixture with no name raises error"""
        with self.assertRaises(ValueError):
            FixtureManager.CreateFixture(self, name=None, flatId=1,
                                         priceValue=5)

    def test_new_fixture_empty_flat(self):
        """Test creating fixture with no flat raises error"""
        with self.assertRaises(ValueError):
            FixtureManager.CreateFixture(self, name='a', flatId=None,
                                         priceValue=300)

    def test_new_fixture_empty_pricevalue(self):
        """Test creating fixture with no price value raises error"""
        with self.assertRaises(ValueError):
            FixtureManager.CreateFixture(self, name='a', flatId=1,
                                         priceValue=None)
