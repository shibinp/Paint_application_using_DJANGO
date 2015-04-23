# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='data',
            field=models.CharField(max_length=1000000),
            preserve_default=True,
        ),
    ]
