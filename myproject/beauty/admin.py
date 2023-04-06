from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'get_logo', 'phone_number', 'register', 'email')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name', "email")
    fields = ('first_name', 'last_name', 'logo', 'get_logo', 'phone_number', 'register', 'email')
    readonly_fields = ('get_logo', 'register')
    save_on_top = True

    def get_logo(self, object):
        if object.logo:
            return mark_safe(f"<img src='{object.logo.url}' width=40>")

    get_logo.short_description = 'LOGO'


class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'address')
    search_fields = ('firs_name', 'last_name', 'company')


class SpecialistReviewAdmin(admin.ModelAdmin):
    list_display = ('specialist', 'date_created', 'reviewer', 'review')


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'price')
    search_fields = ('service_name',)


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('date',)


admin.site.register(Profilis)
admin.site.register(Client, ClientAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(SpecialistServices)
admin.site.register(SpecialistReview, SpecialistReviewAdmin)
