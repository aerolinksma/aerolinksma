# Generated by Django 3.0.2 on 2020-06-13 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttle', '0004_auto_20200612_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='sma_address',
            field=models.CharField(max_length=255, verbose_name='SMA Address'),
        ),
    ]
