# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleships', '0009_auto_20170809_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gameStatus',
            field=models.IntegerField(default=b'5', null=True, db_index=True, blank=True, choices=[(0, b'Active'), (1, b'Waiting for player 1 to set up'), (2, b'Waiting for player 2 to set up'), (3, b'Waiting for player 1'), (4, b'Waiting for player 2'), (5, b'Abandoned'), (6, b'Finished'), (7, b'Waiting for players to join')]),
        ),
    ]
