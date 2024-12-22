from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import BusinessCard

class BusinessCardModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='password123',
            first_name='Test',
            last_name='User'
        )
        self.business_card = BusinessCard.objects.create(
            user=self.user,
            title='Software Engineer',
            company_name='Tech Company',
            location='New York, NY',
            email='testuser@techcompany.com',
            phone_number='123-456-7890',
            website='https://www.techcompany.com'
        )

    def test_business_card_creation(self):
        self.assertEqual(self.business_card.user, self.user)
        self.assertEqual(self.business_card.title, 'Software Engineer')
        self.assertEqual(self.business_card.company_name, 'Tech Company')
        self.assertEqual(self.business_card.location, 'New York, NY')
        self.assertEqual(self.business_card.email, 'testuser@techcompany.com')
        self.assertEqual(self.business_card.phone_number, '123-456-7890')
        self.assertEqual(self.business_card.website, 'https://www.techcompany.com')
        self.assertIsNotNone(self.business_card.created_at)
        self.assertIsNotNone(self.business_card.updated_at)

    def test_business_card_str(self):
        self.assertEqual(str(self.business_card), 'Software Engineer at Tech Company')