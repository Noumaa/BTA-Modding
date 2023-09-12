from django.apps import AppConfig
from django.db.models.signals import post_migrate


class ModsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mods'

    def ready(self):
        from mods import signals
        post_migrate.connect(signals.create_default_categories, sender=self)
        post_migrate.connect(signals.create_default_release_channels, sender=self)
        return super().ready()
