from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Specialist, SpecialistReview


class BaseViewTest(TestCase):
    """Testas puslapio atvaizdavimui"""
    def test_base_view(self):
        response = self.client.get(reverse('base'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beauty/base.html')


class SearchViewTest(TestCase):
    """Testas paieškos funkcijai"""
    def test_search_view(self):
        response = self.client.get(reverse('search') + '?query=test')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beauty/search.html')
        self.assertIn('test', response.content.decode())


class RegistrationViewTest(TestCase):
    """Testas registracijai"""
    def test_registration_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'phone_number': '123456789',
            'email': 'test@example.com',
            'password': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login page


class UpdateProfileViewTest(TestCase):
    """Testas profilio atnaujinimui"""
    def test_update_profile_view(self):
        response = self.client.post(reverse('update_profile'), {
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'updated@example.com',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to profile page


# class SpecialistsByUserListViewTest(TestCase):
#     """Testas vartotojų sąrašo peržiūrai"""
#     def setUp(self):
#         self.client.force_login(User.objects.create_user(username='testuser', password='password'))
#
#     def test_specialists_by_user_list_view(self):
#         response = self.client.get(reverse('profile'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'beauty/user_client.html')


# class SpecialistDetailViewTest(TestCase):
#     """Testas specialisto detaliai"""
#     def test_specialist_detail_view(self):
#         specialist = Specialist.objects.create(first_name='John', last_name='Doe', company='Test Company')
#         response = self.client.get(reverse('specialist_detail', kwargs={'pk': specialist.pk}))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'beauty/specialist_detail.html')


# class SpecialistListViewTest(TestCase):
#     """Testas specialistų sąrašo atvaizdavimui"""
#     def test_specialist_list_view(self):
#         response = self.client.get(reverse('specialist_list'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'beauty/specialist_list.html')


# class UpdateProfilePhotoTest(TestCase):
#     """Testas įkeliant nuotrauką į profilio formą"""
#     def test_update_profile_photo(self):
#         with open('test_image.jpg', 'rb') as file:
#             response = self.client.post(reverse('update_profile'), {
#                 'photo': file,
#             })
#         self.assertEqual(response.status_code, 302)  # Redirect to profile page




# class UserProfileViewTest(TestCase):
#     """Testas vartotojo profilio peržiūrai"""
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='password')
#         self.client.login(username='testuser', password='password')
#
#     def test_user_profile_view(self):
#         response = self.client.get(reverse('view_profile'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'beauty/profile.html')
