from rest_framework import viewsets, routers
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import UserSerializer, ModSerializer, VersionSerializer
from mods.models import Mod, Version
from users.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
class ModViewSet(viewsets.ModelViewSet):
    queryset = Mod.objects.all()
    serializer_class = ModSerializer

    @action(detail=True)
    def download(self, request, pk=None):
        mod: Mod = self.get_object()
        return Response({'url': request.build_absolute_uri(mod.versions.first().file.url)})


class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer
