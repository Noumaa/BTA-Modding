# Generated by Django 4.2.4 on 2023-09-12 16:40

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0023_alter_version_release_channel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='changelog',
            field=markdownx.models.MarkdownxField(blank=True, null=True),
        ),
    ]
