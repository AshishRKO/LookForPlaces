# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popular', '0002_detailplaces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailplaces',
            name='description',
            field=models.TextField(max_length=5000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='places',
            name='description',
            field=models.TextField(max_length=5000),
            preserve_default=True,
        ),
    ]
