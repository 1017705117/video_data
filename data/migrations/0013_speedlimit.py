# Generated by Django 3.1 on 2020-08-23 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_illegalstatistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeedLimit',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('speed', models.IntegerField()),
            ],
        ),
    ]
