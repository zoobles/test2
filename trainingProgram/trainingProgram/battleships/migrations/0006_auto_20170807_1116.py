# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleships', '0005_gameusers_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameusers',
            name='password',
        ),
        migrations.AddField(
            model_name='game',
            name='gameData',
            field=models.TextField(null=True, blank=True),
        ),
    ]
