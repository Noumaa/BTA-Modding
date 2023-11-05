from django.db import models


def launcher_upload_path(instance, filename):
    return f'launcher/{instance.version}/{filename}'


class Launcher(models.Model):
    version = models.CharField(max_length=64, unique=True)
    file = models.FileField(upload_to=launcher_upload_path)
    changelog = models.TextField(blank=True, null=True)
    published = models.DateTimeField(blank=True, auto_now_add=True)

    class Meta:
        ordering = ['-published']
