from django.urls import path

from mods import views

app_name = 'mods'

urlpatterns = [
    path('', views.mods_list, name='list'),
    path('publish', views.mods_create, name='create'),
    path('<str:username>/<slug:mod_slug>', views.mods_detail, name='detail'),
    path('<str:username>/<slug:mod_slug>/<slug:version_slug>', views.version_download, name='version-download'),
]
