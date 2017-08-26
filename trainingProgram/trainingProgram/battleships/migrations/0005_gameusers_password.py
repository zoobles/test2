# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleships', '0004_auto_20170801_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameusers',
            name='password',
            field=models.TextField(null=True, blank=True),
        ),
    ]
