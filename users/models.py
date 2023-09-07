from django.contrib.auth.models import AbstractUser
from django.db import models


def avatar_upload_path(instance, filename):
    return f'avatars/{instance.pk}/{filename}'


class User(AbstractUser):
    avatar = models.ImageField(upload_to=avatar_upload_path, default='avatar_default.png')
