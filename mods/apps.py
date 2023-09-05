from django.apps import AppConfig
from django.db.models.signals import post_migrate


class ModsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mods'

    def ready(self):
        from mods.signals import create_default_categories
        post_migrate.connect(create_default_categories, sender=self)
        return super().ready()
