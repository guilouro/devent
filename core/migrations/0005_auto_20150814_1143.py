# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_event_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='from_day',
        ),
        migrations.RemoveField(
            model_name='event',
            name='to_day',
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(null=True, verbose_name='Come\xe7a em:'),
            preserve_default=True,
        ),
    ]
