# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleships', '0006_auto_20170807_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='gameId',
            field=models.ForeignKey(related_name='gameId', blank=True, to='battleships.GameUsers', null=True),
        ),
    ]
