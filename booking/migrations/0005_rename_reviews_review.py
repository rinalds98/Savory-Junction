# Generated by Django 3.2.18 on 2023-04-06 21:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("booking", "0004_auto_20230406_2126"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Reviews",
            new_name="Review",
        ),
    ]
