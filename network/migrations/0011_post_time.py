# Generated by Django 4.2.7 on 2024-02-11 01:05

from django.db import migrations, models
import network.models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_alter_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.TimeField(default=network.models.get_current_time),
        ),
    ]
