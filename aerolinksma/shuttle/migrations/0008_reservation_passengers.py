# Generated by Django 2.2.6 on 2020-06-19 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttle', '0007_auto_20200615_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='passengers',
            field=models.IntegerField(default=1),
        ),
    ]