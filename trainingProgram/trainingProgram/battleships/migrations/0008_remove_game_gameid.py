# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleships', '0007_game_gameid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='gameId',
        ),
    ]
