# Generated by Django 4.2.4 on 2023-09-12 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0026_loader'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='loaders',
            field=models.ManyToManyField(related_name='versions', to='mods.loader'),
        ),
    ]