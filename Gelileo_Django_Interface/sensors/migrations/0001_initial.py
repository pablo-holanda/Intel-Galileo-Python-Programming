# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LightSensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField(default=0)),
                ('reading_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TemperatureSensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField(default=0)),
                ('reading_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
