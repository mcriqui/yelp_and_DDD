# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yelp_info', '0002_episode_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='date',
        ),
        migrations.AddField(
            model_name='episode',
            name='rating',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
