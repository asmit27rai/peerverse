# Generated by Django 5.0.6 on 2024-06-19 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peerverse', '0007_remove_post_likes_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]