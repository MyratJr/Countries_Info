# Generated by Django 4.0.3 on 2022-05-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0058_rename_image_propertyimage_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='flag',
            field=models.CharField(max_length=9999),
        ),
    ]
