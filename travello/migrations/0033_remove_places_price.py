# Generated by Django 4.0.3 on 2022-05-03 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0032_delete_placeyear'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='price',
        ),
    ]