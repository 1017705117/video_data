# Generated by Django 3.1 on 2020-08-21 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20200821_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trafficflow',
            name='video',
        ),
    ]