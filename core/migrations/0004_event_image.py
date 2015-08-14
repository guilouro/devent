# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150814_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.URLField(max_length=250, null=True, verbose_name='Imagem'),
            preserve_default=True,
        ),
    ]
