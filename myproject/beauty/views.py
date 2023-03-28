from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def base(request):
    return render(request, 'beauty/base.html', {'title': 'Beauty'})


def services(request):
    sevices_list = Services.objects.all()
    return render(request, 'beauty/services.html', {'services': sevices_list})


def user(request):
    pass


def specialist(request):
    specialist_list = Specialist.objects.all()
    return render(request, 'beauty/specialist.html', {'specialist': specialist_list})

def registration(request):
    pass
