# Generated by Django 4.0.3 on 2022-05-07 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0044_alter_places_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='population',
            field=models.CharField(max_length=100),
        ),
    ]
