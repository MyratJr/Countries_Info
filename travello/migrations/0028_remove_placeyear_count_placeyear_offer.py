# Generated by Django 4.0.3 on 2022-05-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0027_alter_placeyear_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placeyear',
            name='Count',
        ),
        migrations.AddField(
            model_name='placeyear',
            name='offer',
            field=models.BooleanField(default=False),
        ),
    ]
