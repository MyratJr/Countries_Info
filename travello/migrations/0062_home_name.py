# Generated by Django 4.0.3 on 2022-05-19 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0061_home_alter_homeslide_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='name',
            field=models.CharField(default='hsjkgdj', max_length=30),
        ),
    ]
