from django.contrib import admin

from mods.models import Mod, Version

# Register your models here.
admin.site.register(Mod)
admin.site.register(Version)
