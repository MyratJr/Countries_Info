# Generated by Django 4.0.3 on 2022-05-19 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0060_homeslide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='homeslide',
            name='property',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='travello.home'),
        ),
    ]
