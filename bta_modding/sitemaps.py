from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from mods.models import Mod, Version


class StaticSitemap(Sitemap):
    priority = 0.8

    def items(self):
        return ["home:home", "users:login"]

    def location(self, obj):
        if obj == "home:home":
            self.priority = 1.0
        else:
            self.priority = 0.8

        return reverse(obj)


class ModSitemap(Sitemap):
    def items(self):
        return Mod.objects.all()

    def lastmod(self, obj):
        latest_version = Version.objects.filter(mod=obj).first()

        if latest_version:
            return latest_version.publish
        return obj.publish
