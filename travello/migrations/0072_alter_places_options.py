# Generated by Django 4.0.3 on 2022-05-23 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0071_remove_places_province'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='places',
            options={'ordering': ['country']},
        ),
    ]