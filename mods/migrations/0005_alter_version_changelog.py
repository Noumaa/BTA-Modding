# Generated by Django 4.2.4 on 2023-08-31 23:28

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0004_alter_version_mod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='changelog',
            field=markdownx.models.MarkdownxField(null=True),
        ),
    ]
