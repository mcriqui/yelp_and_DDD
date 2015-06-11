# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yelp_info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='restaurant',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
