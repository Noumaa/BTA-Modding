from rest_framework import serializers

from mods.models import Mod, Version
from users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'is_staff']


class ModSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mod
        fields = ['pk', 'slug', 'label', 'short_description']


class VersionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Version
        fields = ['slug', 'label', 'changelog', 'file']
