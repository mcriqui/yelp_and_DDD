# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('season', models.IntegerField(null=True, blank=True)),
                ('episode_title', models.CharField(max_length=30, null=True, blank=True)),
                ('city', models.CharField(max_length=30, null=True, blank=True)),
                ('state', models.CharField(max_length=30, null=True, blank=True)),
                ('business_id', models.CharField(max_length=100, null=True, blank=True)),
                ('date', models.DateField()),
            ],
        ),
    ]
