# Generated by Django 4.2.4 on 2023-09-05 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0010_alter_mod_publish_alter_version_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='mod',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
