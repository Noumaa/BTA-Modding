# Generated by Django 4.2.4 on 2023-09-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0014_category_remove_mod_categories_mod_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
    ]
