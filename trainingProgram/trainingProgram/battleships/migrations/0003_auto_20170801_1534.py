# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleships', '0002_auto_20170801_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameusers',
            name='emailAdress',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='gameusers',
            name='username',
            field=models.TextField(null=True, blank=True),
        ),
    ]
