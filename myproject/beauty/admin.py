from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'get_logo', 'phone_number', 'register', 'email')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name', "email")
    ordering = ('-register',)
    fields = ('first_name', 'last_name', 'logo', 'get_logo', 'phone_number', 'register', 'email')
    readonly_fields = ('get_logo', 'register')
    save_on_top = True
    list_editable = ('register',)
    list_per_page = 5

    def get_logo(self, objects):
        if objects.logo:
            return mark_safe(f"<img src='{objects.logo.url}' width=40>")

    get_logo.short_description = 'LOGO'


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'address')
    search_fields = ('firs_name', 'last_name', 'company')


@admin.register(SpecialistReview)
class SpecialistReviewAdmin(admin.ModelAdmin):
    list_display = ('specialist', 'date_created', 'reviewer', 'review')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'price')
    search_fields = ('service_name',)


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('date',)


admin.site.register(Profile)
admin.site.register(SpecialistServices)
admin.site.register(Qualification)
