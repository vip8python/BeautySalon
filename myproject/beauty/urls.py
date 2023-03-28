from django.urls import path
from .views import *

urlpatterns = [
    path('', base, name='base'),
    path('services/', services, name='services'),
    path('users/', user, name='user'),
    path('specialists/', specialist, name='specialist'),
    path('registration/', registration, name='registration'),
]
