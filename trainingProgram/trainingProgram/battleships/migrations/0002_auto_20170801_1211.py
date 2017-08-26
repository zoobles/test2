# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleships', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='gameStatus',
            field=models.IntegerField(default=b'5', null=True, db_index=True, blank=True, choices=[(0, b'Active'), (1, b'Abandoned'), (2, b'Finished'), (3, b'Waiting for player 1'), (4, b'Waiting for player 2'), (5, b'Waiting for players to join')]),
        ),
        migrations.AddField(
            model_name='game',
            name='next_to_move',
            field=models.ForeignKey(related_name='game_next_to_move', blank=True, to='battleships.GameUsers', null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='player_1',
            field=models.ForeignKey(related_name='game_player_1', blank=True, to='battleships.GameUsers', null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='player_1_data',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='game',
            name='player_2',
            field=models.ForeignKey(related_name='game_player_2', blank=True, to='battleships.GameUsers', null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='player_2_data',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='game',
            name='start_time',
            field=models.DateTimeField(db_index=True, auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='gameusers',
            name='createdDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='gameusers',
            name='updatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
