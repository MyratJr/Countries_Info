# Generated by Django 4.0.3 on 2022-05-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0065_alter_homeslide_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='province',
            field=models.BigIntegerField(),
        ),
    ]
