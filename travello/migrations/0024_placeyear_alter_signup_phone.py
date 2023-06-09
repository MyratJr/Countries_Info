# Generated by Django 4.0.3 on 2022-04-28 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0023_alter_signup_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Year', models.IntegerField()),
                ('Count', models.IntegerField()),
                ('Text', models.TextField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='signup',
            name='Phone',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
