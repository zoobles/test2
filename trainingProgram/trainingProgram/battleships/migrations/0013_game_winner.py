# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleships', '0012_auto_20170811_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(blank=True, to='battleships.GameUsers', null=True),
        ),
    ]
