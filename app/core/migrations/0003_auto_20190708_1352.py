# Generated by Django 2.2.3 on 2019-07-08 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190708_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='flat_id',
            new_name='flat',
        ),
    ]
