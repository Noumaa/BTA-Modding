from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from bta_modding import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('home.urls')),
    path('', include('mods.urls')),
    path('markdownx/', include('markdownx.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
