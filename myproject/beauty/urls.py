from django.urls import path
from .views import *

urlpatterns = [
    path('', base, name='base'),
    path('services/', services, name='services'),
    path('clients/', client, name='client'),
    path('search/', search, name='search'),
    path('registration/', registration, name='registration'),
    path('profilis/', profilis, name='profilis'),
    path('my_clients/', SpecialistsByUserListView.as_view(), name='user_client'),
    path('myclients/<int:pk>', SpecialistByUserDetailView.as_view(), name='client_detail'),
    path('specialists/', SpecialistListView.as_view(), name='specialist'),
    path('specialists/<int:pk>/', SpecialistDetailView.as_view(), name='specialist_detail'),
    path('register/', register, name='register')
]
