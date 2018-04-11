# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hist_price', '0006_auto_20180409_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(max_length=10, default='NEW', choices=[('NEW', 'New'), ('OK', 'Ok'), ('ERROR', 'Error'), ('NOT_FOUND', 'Not found')]),
        ),
    ]
