from django.test import TestCase
from django.utils import timezone

from .models import Client, Specialist, Profile, SpecialistReview, Services
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime


class ClientModelTest(TestCase):
    def setUp(self):
        self.client = Client.objects.create(
            first_name='John',
            last_name='Doe',
            phone_number='123456789',
            email='john@example.com',
            password='password'
        )

    def test_client_str(self):
        self.assertEqual(str(self.client), 'John Doe')

    def test_get_absolute_url(self):
        self.assertEqual(self.client.get_absolute_url(), reverse('client_detail', args=[str(self.client.id)]))


class SpecialistModelTest(TestCase):
    def setUp(self):
        self.specialist = Specialist.objects.create(
            company='Company',
            first_name='Jane',
            last_name='Doe',
            descriptions='Description',
            address='Address',
            register=datetime.now()
        )

    def test_specialist_str(self):
        self.assertEqual(str(self.specialist), 'Company')


class SpecialistReviewTest(TestCase):
    def setUp(self):
        self.specialist_review = SpecialistReview.objects.create(
            date_created=timezone.now(),
            review='big text'
        )

    def test_client_str(self):
        self.assertEqual(str(self.specialist_review), 'big text')


class ServicesTest(TestCase):
    def setUp(self):
        self.services = Services.objects.create(
            service_name='service',
            time=240,
            price=125
        )

    def test_client_str(self):
        self.assertEqual(str(self.services), 'service')
