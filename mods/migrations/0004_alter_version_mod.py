# Generated by Django 4.2.4 on 2023-08-31 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0003_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='mod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='mods.mod'),
        ),
    ]
