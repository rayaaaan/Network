# Generated by Django 4.2.7 on 2024-02-11 01:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_rename_poste_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date(2024, 2, 11)),
        ),
    ]
