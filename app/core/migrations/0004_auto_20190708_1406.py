# Generated by Django 2.2.3 on 2019-07-08 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190708_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='flat',
            new_name='flat_id',
        ),
    ]
