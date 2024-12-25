from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import BusinessCard
from .forms import BusinessCardForm
from django.urls import reverse

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
            first_name='John',
            last_name='Doe',
            title='Software Engineer',
            company_name='Tech Company',
            location='New York, NY',
            email='testuser@techcompany.com',
            phone_number='123-456-7890',
            website='https://www.techcompany.com'
        )

    def test_business_card_creation(self):
        self.assertEqual(self.business_card.user, self.user)
        self.assertEqual(self.business_card.first_name, 'John')
        self.assertEqual(self.business_card.last_name, 'Doe')
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

    def test_get_absolute_url(self):
        self.assertEqual(self.business_card.get_absolute_url(), reverse('business_card_detail', kwargs={'uuid': self.business_card.uuid}))

class BusinessCardFormTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='password123',
            first_name='Test',
            last_name='User'
        )

    def test_valid_form(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'title': 'Software Engineer',
            'company_name': 'Tech Company',
            'location': 'New York, NY',
            'email': 'testuser@techcompany.com',
            'phone_number': '123-456-7890',
            'website': 'https://www.techcompany.com'
        }
        form = BusinessCardForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'first_name': '',
            'last_name': '',
            'title': '',
            'company_name': '',
            'location': '',
            'email': 'invalid-email',
            'phone_number': '',
            'website': ''
        }
        form = BusinessCardForm(data=data)
        self.assertFalse(form.is_valid())

class BusinessCardViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='password123',
            first_name='Test',
            last_name='User'
        )
        self.client.login(email='testuser@example.com', password='password123')
        self.business_card = BusinessCard.objects.create(
            user=self.user,
            first_name='John',
            last_name='Doe',
            title='Software Engineer',
            company_name='Tech Company',
            location='New York, NY',
            email='testuser@techcompany.com',
            phone_number='123-456-7890',
            website='https://www.techcompany.com'
        )

    def test_dashboard_view(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')

    def test_business_card_detail_view(self):
        response = self.client.get(reverse('business_card_detail', kwargs={'uuid': self.business_card.uuid}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/business_card_detail.html')

    def test_add_business_card_view(self):
        response = self.client.get(reverse('add_business_card'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/add_business_card.html')

        data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'title': 'Product Manager',
            'company_name': 'Another Tech Company',
            'location': 'San Francisco, CA',
            'email': 'janesmith@anothertechcompany.com',
            'phone_number': '987-654-3210',
            'website': 'https://www.anothertechcompany.com'
        }
        response = self.client.post(reverse('add_business_card'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))
        self.assertEqual(BusinessCard.objects.count(), 2)

    def test_edit_business_card_view(self):
        response = self.client.get(reverse('edit_business_card', kwargs={'uuid': self.business_card.uuid}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/edit_business_card.html')

        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'title': 'Senior Software Engineer',
            'company_name': 'Tech Company',
            'location': 'New York, NY',
            'email': 'testuser@techcompany.com',
            'phone_number': '123-456-7890',
            'website': 'https://www.techcompany.com'
        }
        response = self.client.post(reverse('edit_business_card', kwargs={'uuid': self.business_card.uuid}), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))
        self.business_card.refresh_from_db()
        self.assertEqual(self.business_card.title, 'Senior Software Engineer')

    def test_delete_business_card_view(self):
        response = self.client.post(reverse('delete_business_card', kwargs={'uuid': self.business_card.uuid}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))
        self.assertEqual(BusinessCard.objects.count(), 0)