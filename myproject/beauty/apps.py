from django.apps import AppConfig


class BeautyConfig(AppConfig):
    verbose_name = 'ADMINISTRATION'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'beauty'

    def ready(self):
        from .signals import create_profile, save_profile
