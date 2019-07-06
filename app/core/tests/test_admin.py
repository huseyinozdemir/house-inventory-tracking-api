from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from core.models import Building

from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.building = Building.objects.create_building(name='A3')
        self.admin_user = get_user_model().objects.create_superuser(
            email='huseyin@pythontr.com',
            password='password123',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='aba@ea.net',
            password='password123',
            name='Test user'
        )

    def test_user_listed(self):
        """User list from user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_user_create_page(self):
        """Test create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_building_listed(self):
        """Building list from user page"""
        url = reverse('admin:core_building_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.building.name)

    def test_building_change_page(self):
        """Test that the building edit page works"""
        url = reverse('admin:core_building_change', args=[self.building.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_building_create_page(self):
        """Test create building page works"""
        url = reverse('admin:core_building_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
