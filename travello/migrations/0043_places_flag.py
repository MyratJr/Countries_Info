# Generated by Django 4.0.3 on 2022-05-07 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0042_alter_places_continent_alter_places_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='flag',
            field=models.ImageField(default='germany.jpg', upload_to=''),
        ),
    ]
