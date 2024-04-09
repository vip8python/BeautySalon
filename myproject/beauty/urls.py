from django.urls import path, re_path
from .views import base, services, client, search, registration, SpecialistsByUserListView, SpecialistByUserDetailView, \
    SpecialistListView, SpecialistDetailView, register, update_profile, blog, show_category, specialist

urlpatterns = [
    path('', base, name='base'),
    path('services/', services, name='services'),
    path('clients/', client, name='client'),
    path('search/', search, name='search'),
    path('registration/', registration, name='registration'),
    path('profile/', update_profile, name='update_profile'),
    path('update_profile/', update_profile, name='profile'),
    path('my_clients/', SpecialistsByUserListView.as_view(), name='user_client'),
    path('my_clients/<int:pk>', SpecialistByUserDetailView.as_view(), name='client_detail'),
    path('specialists/', SpecialistListView.as_view(), name='specialist'),
    path('specialists/<int:pk>/', SpecialistDetailView.as_view(), name='specialist_detail'),
    path('register/', register, name='register'),
    re_path(r'^blog/', blog, name='blog'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('specialist_active/', specialist, name='active_specialist'),
]
