# Generated by Django 3.0.8 on 2020-07-01 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sites',
            new_name='Site',
        ),
    ]