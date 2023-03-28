from django.urls import path
from .views import *

urlpatterns = [
    path('', base, name='base'),
    path('services/', services, name='services'),
    path('users/', user, name='user'),
    path('search/', search, name='search'),
    path('registration/', registration, name='registration'),

    path('specialists/', SpecialistListView.as_view(), name='specialist'),
    path('specialists/<int:pk>/', SpecialistDetailView.as_view(), name='specialist_detail'),
]
