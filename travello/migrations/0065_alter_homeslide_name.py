# Generated by Django 4.0.3 on 2022-05-19 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0064_slideimage_remove_homeslide_image_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeslide',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
