# Generated by Django 5.0.2 on 2024-04-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_remove_users_cities_users_cities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='cities',
        ),
        migrations.AddField(
            model_name='users',
            name='cities',
            field=models.ManyToManyField(to='userapp.city'),
        ),
    ]
