# Generated by Django 5.0.2 on 2024-04-24 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_users_cities_alter_users_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='cities',
        ),
        migrations.AddField(
            model_name='users',
            name='cities',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='userapp.city'),
            preserve_default=False,
        ),
    ]
