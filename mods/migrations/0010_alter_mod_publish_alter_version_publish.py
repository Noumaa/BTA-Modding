# Generated by Django 4.2.4 on 2023-09-02 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0009_alter_mod_options_alter_version_options_mod_publish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mod',
            name='publish',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='version',
            name='publish',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
