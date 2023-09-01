from django.db import models
from django.utils.text import slugify
from markdownx.models import MarkdownxField

from django.conf import settings


def version_upload_path(instance, filename):
    return f'mods/{instance.mod.pk}/{instance.slug}/{filename}'


def avatar_upload_path(instance, filename):
    return f'mods/{instance.mod.pk}/{filename}'


# Create your models here.
class Mod(models.Model):
    label = models.CharField(max_length=48)
    slug = models.SlugField(null=False, unique=True)
    short_description = models.CharField(max_length=128)
    logo = models.ImageField(upload_to=avatar_upload_path, default="assets/images/mod_default.png")
    description = MarkdownxField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mods', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.label)
        return super().save(*args, **kwargs)


class Version(models.Model):
    mod = models.ForeignKey(Mod, related_name='versions', on_delete=models.CASCADE)
    label = models.CharField(max_length=48)
    slug = models.SlugField(null=False)
    changelog = MarkdownxField(null=True)
    file = models.FileField(upload_to=version_upload_path)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.label)
        return super().save(*args, **kwargs)
