from django import forms
from django.contrib.auth.models import User
from .models import SpecialistReview, Profile
from captcha.fields import CaptchaField


class SpecialistReviewForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = SpecialistReview
        fields = ('review', 'specialist', 'reviewer', 'captcha')
        widgets = {'specialist': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']
