# Generated by Django 3.1 on 2020-08-24 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0018_auto_20200824_1931'),
    ]

    operations = [
        migrations.DeleteModel(
            name='IllegalImage',
        ),
        migrations.DeleteModel(
            name='SpeedLimit',
        ),
        migrations.AddField(
            model_name='illegaldata',
            name='videoId',
            field=models.IntegerField(default='1'),
        ),
    ]