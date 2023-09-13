from django.db import models
from django.utils.text import slugify
from markdownx.models import MarkdownxField
from django.utils.translation import gettext_lazy as _

from django.conf import settings

from mods.slugify import unique_slugify


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

    def get_absolute_url(self):
        return f"/{self.user.username}/{self.slug}/"

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.label)
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


class ExternalLinks(models.Model):
    mod = models.ForeignKey(Mod, related_name='links', on_delete=models.CASCADE)
    issue_tracker = models.URLField(default='', blank=True)
    source_code = models.URLField(default='', blank=True)
    wiki_page = models.URLField(default='', blank=True)
    discord_invite = models.URLField(default='', blank=True)
    donation_links = models.URLField(default='', blank=True)

    def get_all_urls(self):
        urls = []

        fields = [field for field in self._meta.get_fields() if isinstance(field, models.URLField)]

        for field in fields:
            url = getattr(self, field.name)
            if url:
                urls.append([field.name, url])

        return urls


class ReleaseChannel(models.Model):
    label = models.CharField(max_length=64)
    color = models.CharField(max_length=7)

    @classmethod
    def get_default(cls):
        release_channel, created = cls.objects.get_or_create(
            label='Release',
        )
        return release_channel.pk

    def __str__(self) -> str:
        return self.label


class Loader(models.Model):
    label = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.label


class GameVersion(models.Model):
    label = models.CharField(max_length=16)

    @classmethod
    def get_latest(cls):
        return cls.objects.get_or_create(label='1.7.7.0_02')[0].pk

    def __str__(self) -> str:
        return self.label


class Version(models.Model):
    mod = models.ForeignKey(Mod, related_name='versions', on_delete=models.CASCADE)

    label = models.CharField(max_length=48)
    slug = models.SlugField(null=False)

    changelog = MarkdownxField(null=True, blank=True)
    file = models.FileField(upload_to=version_upload_path)

    game_version = models.ForeignKey(GameVersion, related_name='versions', on_delete=models.CASCADE)
    loaders = models.ManyToManyField(Loader, related_name='versions')
    release_channel = models.ForeignKey(ReleaseChannel, related_name='versions', default=ReleaseChannel.get_default, on_delete=models.CASCADE)

    publish = models.DateTimeField(auto_now_add=True)
    downloads = models.IntegerField(blank=True, default=0)

    class Meta:
        ordering = ["-publish"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.label)
        if not self.release_channel:
            self.release_channel = ReleaseChannel.objects.get(label='Release')
        return super().save(*args, **kwargs)
