# Generated by Django 5.0.6 on 2024-06-18 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peerverse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
