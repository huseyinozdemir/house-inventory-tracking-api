# Generated by Django 2.2.3 on 2019-07-07 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190707_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='price_value',
            field=models.FloatField(default=0),
        ),
    ]
