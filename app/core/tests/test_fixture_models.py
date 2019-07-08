# from django.contrib.auth import get_user_model

from django.test import TestCase
from core.models import Fixture


class FixtureModelTests(TestCase):

    def test_new_fixture_empty_name(self):
        """Test creating fixture with no name raises error"""
        with self.assertRaises(ValueError):
            Fixture.objects.create_fixture(
                name=None, user=1, room=1,
                price_value=5
            )

    def test_new_fixture_empty_user(self):
        """Test creating fixture with no user raises error"""
        with self.assertRaises(ValueError):
            Fixture.objects.create_fixture(
                name=1, user=None, room=1,
                price_value=5
            )

    def test_new_fixture_empty_flat(self):
        """Test creating fixture with no flat raises error"""
        with self.assertRaises(ValueError):
            Fixture.objects.create_fixture(
                name='a', user=4, room=None,
                price_value=300
            )

    def test_new_fixture_empty_pricevalue(self):
        """Test creating fixture with no price value raises error"""
        with self.assertRaises(ValueError):
            Fixture.objects.create_fixture(
                name='a', user=3, room=1,
                price_value=None
            )
