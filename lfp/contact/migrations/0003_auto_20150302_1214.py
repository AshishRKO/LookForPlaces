# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20150301_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='companyName',
            field=models.CharField(max_length=80),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='subject',
            field=models.CharField(max_length=80),
            preserve_default=True,
        ),
    ]
