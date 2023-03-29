from django import forms
from .models import *
from captcha.fields import CaptchaField

class SpecialistReviewForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = SpecialistReview
        fields = ('review', 'specialist', 'reviewer', 'captcha')
        widgets = {'specialist': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}
