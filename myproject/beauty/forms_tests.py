from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .forms import SpecialistReviewForm, UserUpdateForm, ProfileUpdateForm
from .models import Specialist


class TestForms(TestCase):

    # def test_specialist_review_form_valid_data(self):
    #     # Sukurkite specialistą ir recenzentą
    #     specialist = Specialist.objects.create(company='Apple')
    #     reviewer = User.objects.create(username='reviewer')
    #     captcha_value = 'abcd'
    #
    #     form = SpecialistReviewForm(data={
    #         'review': 'Good service',
    #         'specialist': specialist.id,
    #         'reviewer': reviewer.id,
    #         'captcha': captcha_value
    #     })
    #
    #     self.assertTrue(form.is_valid(), form.errors)

    def test_specialist_review_form_no_data(self):
        form = SpecialistReviewForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_user_update_form_email_field(self):
        form = UserUpdateForm(data={'email': 'test@example.com', 'username': 'test_user'})

        self.assertTrue(form.is_valid())

    def test_user_update_form_no_data(self):
        form = UserUpdateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_profile_update_form_valid_data(self):

        with open('beauty/media/profile_pics/default.png', 'rb') as f:
            test_image = SimpleUploadedFile("test.jpg", f.read(), content_type="image/jpeg")

        form = ProfileUpdateForm(data={}, files={'photo': test_image})

        self.assertTrue(form.is_valid(), form.errors)


