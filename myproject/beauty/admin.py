from django.contrib import admin

from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'logo', 'phone_number', 'register', 'email')



admin.site.register(User)
admin.site.register(Services)
admin.site.register(Specialist)
admin.site.register(Registration)
admin.site.register(SpecialistServices)

