# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hist_price', '0005_auto_20180408_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('url', models.URLField(max_length=1000)),
            ],
        ),
        migrations.AlterModelOptions(
            name='pricehistory',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RemoveField(
            model_name='item',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='item',
            name='retailprice',
        ),
        migrations.RemoveField(
            model_name='pricehistory',
            name='date',
        ),
        migrations.AddField(
            model_name='item',
            name='current_price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='last_price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='price_changes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='price_percentage_variance',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='item',
            name='price_raw_variance',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(default='2018-04-09', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pricehistory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 9, 15, 11, 14, 2414, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='pricehistory',
            name='item',
            field=models.ForeignKey(related_name='price_history', to='hist_price.Item'),
        ),
        migrations.AlterField(
            model_name='pricehistory',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(related_name='images', to='hist_price.Item'),
        ),
    ]
