# Generated by Django 4.2.4 on 2023-11-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launcher', '0003_alter_launcher_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launcher',
            name='version',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
