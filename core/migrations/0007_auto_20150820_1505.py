# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150814_1350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['start_date'], 'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
        migrations.AddField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=datetime.date(2015, 8, 20), verbose_name='Criado em:', auto_now_add=True),
            preserve_default=False,
        ),
    ]
