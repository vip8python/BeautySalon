from django import forms
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

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


class CommentForm(forms.Form):
    username = forms.CharField(max_length=50, required=False)
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    register = forms.DateField(required=False, input_formats=['%Y-%m-%d'],
                               widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(required=False, validators=[EmailValidator()])
