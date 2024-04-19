from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('services/', views.services, name='services'),
    path('clients/', views.client, name='client'),
    path('comment/', views.comment, name='comment'),
    path('search/', views.search, name='search'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.update_profile, name='update_profile'),
    path('update_profile/', views.update_profile, name='profile'),
    path('my_clients/', views.SpecialistsByUserListView.as_view(), name='user_client'),
    path('my_clients/<int:pk>', views.SpecialistByUserDetailView.as_view(), name='client_detail'),
    path('specialists/', views.SpecialistListView.as_view(), name='specialist'),
    path('specialists/<int:pk>/', views.SpecialistDetailView.as_view(), name='specialist_detail'),
    path('register/', views.register, name='register'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    path('specialist_active/', views.specialist, name='active_specialist'),
    re_path(r'^blog/', views.blog, name='blog'),
]
