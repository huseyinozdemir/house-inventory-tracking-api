from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase


from rest_framework import status
from rest_framework.test import APIClient


from core.models import Building


from building.serializers import BuildingSerializer


BUILDINGS_URL = reverse('building:building-list')


class PublicBuildingsApiTests(TestCase):
    """Test thje publicly available buildings API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving buildings"""
        res = self.client.get(BUILDINGS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateBuildingsApiTests(TestCase):
    """Test the authorized user buildings API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@pythontr.com',
            '123qwe'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_buildings(self):
        """Test retrieving buildings"""
        Building.objects.create(user=self.user, name='a3 blok')
        Building.objects.create(user=self.user, name='b7 blok')

        res = self.client.get(BUILDINGS_URL)

        buildings = Building.objects.all().order_by('-name')
        serializer = BuildingSerializer(buildings, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
