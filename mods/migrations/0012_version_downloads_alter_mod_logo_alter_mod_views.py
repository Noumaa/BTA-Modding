# Generated by Django 4.2.4 on 2023-09-05 03:22

from django.db import migrations, models
import mods.models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0011_mod_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='downloads',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mod',
            name='logo',
            field=models.ImageField(default='mod_default.png', upload_to=mods.models.avatar_upload_path),
        ),
        migrations.AlterField(
            model_name='mod',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
