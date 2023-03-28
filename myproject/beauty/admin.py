from django.contrib import admin

from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'logo', 'phone_number', 'register', 'email')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name', "email")
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'address')
    search_fields = ('firs_name', 'last_name', 'company')

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'price')
    search_fields = ('service_name',)

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('data', )



admin.site.register(User, UserAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Registration)
admin.site.register(SpecialistServices)

