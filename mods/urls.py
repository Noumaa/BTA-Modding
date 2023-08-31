from django.urls import path

from mods import views

app_name = 'mods'

urlpatterns = [
    path('', views.mods_list, name='list'),
    path('publish', views.mods_create, name='create'),
    path('<slug:mod_slug>', views.mods_detail, name='detail'),
]
