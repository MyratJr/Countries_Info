# Generated by Django 4.0.3 on 2022-04-27 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0014_remove_signup_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='Phone',
            field=models.IntegerField(null=True),
        ),
    ]
