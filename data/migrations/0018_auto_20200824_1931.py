# Generated by Django 3.1 on 2020-08-24 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0017_auto_20200824_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoSpeed',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('upload_time', models.CharField(max_length=100)),
                ('video_path', models.CharField(max_length=100)),
                ('speed', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
