# Generated by Django 3.0.2 on 2020-06-25 03:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shuttle', '0012_auto_20200625_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
