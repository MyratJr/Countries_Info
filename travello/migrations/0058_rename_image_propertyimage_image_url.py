# Generated by Django 4.0.3 on 2022-05-16 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0057_alter_propertyimage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertyimage',
            old_name='image',
            new_name='image_url',
        ),
    ]
