# Generated by Django 4.0.3 on 2022-05-19 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0063_alter_home_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=9999)),
            ],
        ),
        migrations.RemoveField(
            model_name='homeslide',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='homeslide',
            name='property',
        ),
        migrations.AddField(
            model_name='homeslide',
            name='name',
            field=models.CharField(default=34, max_length=30),
        ),
        migrations.DeleteModel(
            name='Home',
        ),
        migrations.AddField(
            model_name='slideimage',
            name='property',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='travello.homeslide'),
        ),
    ]