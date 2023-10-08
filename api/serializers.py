from rest_framework import serializers

from mods.models import Mod, Version
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'is_staff']


class ModSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mod
        fields = ['pk', 'slug', 'label', 'short_description']


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ['pk', 'mod', 'slug', 'label', 'changelog', 'file']
