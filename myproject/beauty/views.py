from django.http import HttpResponse
from django.shortcuts import render


def base(request):
    return render(request, 'beauty/base.html', {'title': 'Beauty'})


def services(request):
    pass


def user(request):
    pass


def specialist(request):
    pass

def registration(request):
    pass
