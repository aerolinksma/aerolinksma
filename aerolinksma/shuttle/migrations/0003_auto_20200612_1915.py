# Generated by Django 3.0.2 on 2020-06-12 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shuttle', '0002_client_reservation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['-created_at']},
        ),
    ]
