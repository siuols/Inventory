# Generated by Django 2.1.7 on 2019-03-01 13:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0010_auto_20190301_1311'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Released',
            new_name='Release',
        ),
    ]