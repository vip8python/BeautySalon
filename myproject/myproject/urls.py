from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from beauty.views import page_not_found

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('beauty.urls')),
                  path('users/', include('users.urls', namespace='users')),
                  path('captcha/', include('captcha.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('__debug__/', include('debug_toolbar.urls')),
              ] + (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
                   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

handler404 = page_not_found
admin.site.site_header = 'Beauty salon'
admin.site.index_title = 'Beauty salon administration'
