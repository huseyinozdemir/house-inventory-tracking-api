from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'huseyin@pythontr.com'
        password = 'TestSifre1234'
        user = get_user_model().objects.CreateUser(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password), True)

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'huseyin@PYTHONTR.com'
        user = get_user_model().objects.CreateUser(email, 'deneme321')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.CreateUser(None, 'obs4455')

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.CreateSuperuser(
            'test@pythontr.com',
            'test123'
        )
        self.assertTrue(user.isSuperuser)
        self.assertTrue(user.isStaff)
