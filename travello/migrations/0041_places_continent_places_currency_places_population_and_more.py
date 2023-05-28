# Generated by Django 4.0.3 on 2022-05-07 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0040_srch'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='continent',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='places',
            name='currency',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='places',
            name='population',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='places',
            name='president',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='places',
            name='square',
            field=models.CharField(default=0, max_length=100),
        ),
    ]