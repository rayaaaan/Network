# Generated by Django 4.2.7 on 2024-02-11 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_alter_user_email_alter_user_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Poste',
            new_name='Post',
        ),
    ]
