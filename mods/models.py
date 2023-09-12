from django.db import models
from django.utils.text import slugify
from markdownx.models import MarkdownxField
from django.utils.translation import gettext_lazy as _

from django.conf import settings


def version_upload_path(instance, filename):
    return f'mods/{instance.mod.pk}/{instance.slug}/{filename}'


def avatar_upload_path(instance, filename):
    return f'mods/{instance.pk}/{filename}'


class Category(models.Model):
    label = models.CharField(max_length=48)
    slug = models.SlugField(null=False, unique=True)
    icon = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.label)
        return super().save(*args, **kwargs)


# Create your models here.
class Mod(models.Model):
    label = models.CharField(max_length=48)
    logo = models.ImageField(upload_to=avatar_upload_path, default="mod_default.png")
    short_description = models.CharField(max_length=128)
    description = MarkdownxField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mods', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    slug = models.SlugField(null=False, unique=True)
    publish = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ["-publish"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.label)
        return super().save(*args, **kwargs)

    def get_downloads(self):
        count = 0
        for version in self.versions.all():
            count += version.downloads
        return count

    def get_categories_pk(self):
        categories_pk = []
        for category in self.categories.all():
            categories_pk += [category.pk]
        return categories_pk


class Version(models.Model):
    mod = models.ForeignKey(Mod, related_name='versions', on_delete=models.CASCADE)
    label = models.CharField(max_length=48)
    slug = models.SlugField(null=False)
    changelog = MarkdownxField(null=True)
    file = models.FileField(upload_to=version_upload_path)
    publish = models.DateTimeField(auto_now_add=True)
    downloads = models.IntegerField(blank=True, default=0)

    class Meta:
        ordering = ["-publish"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.label)
        return super().save(*args, **kwargs)
