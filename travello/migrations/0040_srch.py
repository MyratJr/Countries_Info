# Generated by Django 4.0.3 on 2022-05-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0039_delete_sdjh'),
    ]

    operations = [
        migrations.CreateModel(
            name='srch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
            ],
        ),
    ]
