from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views import UserViewSet, ModViewSet, VersionViewSet

app_name = 'api'

router = routers.DefaultRouter()

# router.register(r'users', UserViewSet)
router.register(r'mods', ModViewSet)
router.register(r'versions', VersionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token)
]
