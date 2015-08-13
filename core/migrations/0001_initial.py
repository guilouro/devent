# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='T\xedtulo')),
                ('from_day', models.DateTimeField(verbose_name='De')),
                ('to_day', models.DateTimeField(verbose_name='To')),
                ('local', models.CharField(max_length=200, verbose_name='Local')),
                ('address', models.CharField(max_length=200, verbose_name='Endere\xe7o')),
                ('price', models.CharField(max_length=20, verbose_name='Pre\xe7o')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
