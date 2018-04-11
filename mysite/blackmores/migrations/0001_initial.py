# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BLImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('url', models.URLField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='BLPriceHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('price', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='BLProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=500, blank=True, null=True)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('manufacturer', models.CharField(max_length=255, null=True)),
                ('manufacturer_code', models.CharField(max_length=255, null=True)),
                ('url', models.URLField(max_length=1000, blank=True, null=True)),
                ('status', models.CharField(max_length=10, default='NEW', choices=[('NEW', 'New'), ('OK', 'Ok'), ('ERROR', 'Error'), ('NOT_FOUND', 'Not found')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('visited_at', models.DateTimeField(auto_now=True)),
                ('current_price', models.FloatField(null=True)),
                ('last_price', models.FloatField(null=True)),
                ('price_raw_variance', models.FloatField(null=True)),
                ('price_percentage_variance', models.FloatField(default=0.0)),
                ('price_changes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='blpricehistory',
            name='product',
            field=models.ForeignKey(related_name='price_history', to='blackmores.BLProduct'),
        ),
        migrations.AddField(
            model_name='blimage',
            name='product',
            field=models.ForeignKey(related_name='images', to='blackmores.BLProduct'),
        ),
    ]
