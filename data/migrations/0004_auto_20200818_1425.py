# Generated by Django 3.1 on 2020-08-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_illegaldata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='illegaldata',
            name='img',
            field=models.CharField(max_length=70),
        ),
    ]
