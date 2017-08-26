# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleships', '0011_auto_20170811_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='hits',
        ),
        migrations.RemoveField(
            model_name='game',
            name='misses',
        ),
    ]
