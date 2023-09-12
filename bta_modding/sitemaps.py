from django.contrib.sitemaps import Sitemap
from django.db.models import Max

from mods.models import Mod, Version


class ModSitemap(Sitemap):
    def items(self):
        return Mod.objects.all()


    def lastmod(self, obj):
        latest_version = Version.objects.filter(mod=obj).first()

        if latest_version:
            return latest_version.publish
        return obj.publish
