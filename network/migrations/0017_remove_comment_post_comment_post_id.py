# Generated by Django 4.2.7 on 2024-02-11 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0016_alter_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.IntegerField(default=0),
        ),
    ]
