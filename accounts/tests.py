from django.test import TestCase
from .models import CustomUser, Organization

class OrganizationModelTest(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(name="Test Organization")

    def test_organization_creation(self):
        self.assertEqual(self.organization.name, "Test Organization")
        self.assertIsNotNone(self.organization.created_at)
        self.assertIsNotNone(self.organization.updated_at)

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(name="Test Organization")
        self.user = CustomUser.objects.create(
            email="testuser@example.com",
            password="password123",
            first_name="Test",
            last_name="User",
            organization=self.organization,
            role="user"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")
        self.assertEqual(self.user.organization.name, "Test Organization")
        self.assertEqual(self.user.role, "user")
        self.assertIsNotNone(self.user.date_joined)
        self.assertIsNotNone(self.user.last_login)
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)