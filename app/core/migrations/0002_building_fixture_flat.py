# Generated by Django 2.2.3 on 2019-07-05 17:48

from django.db import migrations, models
from django.db.models import deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isDelete', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isDelete', models.BooleanField(default=True)),
                ('buildingID',
                    models.ForeignKey(on_delete=deletion.DO_NOTHING,
                                      to='core.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isDelete', models.BooleanField(default=True)),
                ('flatID',
                    models.ForeignKey(on_delete=deletion.DO_NOTHING,
                                      to='core.Flat')),
            ],
        ),
    ]
