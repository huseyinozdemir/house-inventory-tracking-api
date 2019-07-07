from django.test import TestCase
from core.models import Fixture, Flat, Building


def sample_building(name="A2"):
    """Create a sample building"""
    return Building.objects.create_building(name)


def sample_flat(name="A2"):
    """Create a sample building"""
    return Flat.objects.create_flat(name, sample_building())


class FixtureModelTests(TestCase):

    def test_new_fixture_empty_name(self):
        """Test creating fixture with no name raises error"""
        with self.assertRaises(ValueError):
            Fixture.objects.create_fixture(name=None, flat_id=1,
                                           price_value=5)

    def test_new_fixture_empty_flat(self):
        """Test creating fixture with no flat raises error"""
        with self.assertRaises(ValueError):
            Fixture.objects.create_fixture(name='a', flat_id=None,
                                           price_value=300)

    def test_new_fixture_empty_pricevalue(self):
        """Test creating fixture with no price value raises error"""
        with self.assertRaises(ValueError):
            Fixture.objects.create_fixture(name='a', flat_id=1,
                                           price_value=None)

    def test_fixture_str(self):
        """Test the fixture string representation"""
        fixture = Fixture.objects.create_fixture(
            name='Buzdolabi',
            flat_id=sample_flat(),
            price_value=10
        )

        self.assertEqual(str(fixture), fixture.name)
