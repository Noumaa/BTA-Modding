# Generated by Django 4.2.4 on 2023-10-09 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0028_alter_version_game_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('FE', 'Feature'), ('SI', 'Side')], default='FE', max_length=2),
        ),
    ]