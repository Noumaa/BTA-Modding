from django.urls import path

from mods import views

app_name = 'mods'

urlpatterns = [
    path('mods/', views.ModListView.as_view(), name='list'),
    path('mods/publish', views.mods_create, name='create'),

    path('<str:username>/<slug:mod_slug>', views.mods_detail, name='detail'),
    path('<str:username>/<slug:mod_slug>/settings', views.mods_edit, name='edit'),

    path('<str:username>/<slug:mod_slug>/versions', views.version_list, name='version-list'),
    path('<str:username>/<slug:mod_slug>/versions/publish', views.version_create, name='version-create'),

    path('<str:username>/<slug:mod_slug>/version/<slug:version_slug>', views.version_detail, name='version-detail'),
    path('<str:username>/<slug:mod_slug>/version/<slug:version_slug>/download', views.version_download, name='version-download'),
]
