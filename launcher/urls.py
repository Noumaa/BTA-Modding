from django.urls import path

from launcher import views

app_name = 'launcher'

urlpatterns = [
    path('launcher/', views.home, name='detail'),
    path('launcher/upload', views.upload, name='upload'),
    # path('launcher/edit', views.edit, name='detail'),
    path('api/launcher/latest', views.api_version, name='_version'),
]
