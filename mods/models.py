from django.db import models
from markdownx.models import MarkdownxField


# Create your models here.
class Mod(models.Model):
    label = models.CharField(max_length=48)
    short_description = models.CharField(max_length=128)
    description = MarkdownxField()
