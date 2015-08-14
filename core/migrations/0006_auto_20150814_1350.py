# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150814_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='address',
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.CharField(max_length=20, null=True, verbose_name='Pre\xe7o'),
        ),
    ]
