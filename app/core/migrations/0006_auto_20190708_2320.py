# Generated by Django 2.2.3 on 2019-07-08 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190708_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='fixture',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='room',
            name='is_delete',
        ),
    ]
