# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleships', '0003_auto_20170801_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameusers',
            name='firstname',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='gameusers',
            name='lastname',
            field=models.TextField(null=True, blank=True),
        ),
    ]
