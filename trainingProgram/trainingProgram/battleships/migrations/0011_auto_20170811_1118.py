# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleships', '0010_auto_20170809_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='gameData',
            new_name='hits',
        ),
        migrations.AddField(
            model_name='game',
            name='misses',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='gameStatus',
            field=models.IntegerField(default=b'5', null=True, db_index=True, blank=True, choices=[(0, b'Active'), (1, b'Waiting for player 1 to set up'), (2, b'Waiting for player 2 to set up'), (3, b'Waiting for player 1 to shoot'), (4, b'Waiting for player 2 to shoot'), (5, b'Abandoned'), (6, b'Finished'), (7, b'Waiting for players to join')]),
        ),
    ]
