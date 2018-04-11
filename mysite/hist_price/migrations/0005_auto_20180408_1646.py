# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hist_price', '0004_auto_20180328_0552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricehistory',
            old_name='Item',
            new_name='item',
        ),
    ]
