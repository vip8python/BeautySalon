from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Services)
admin.site.register(Specialist)
admin.site.register(Data)

