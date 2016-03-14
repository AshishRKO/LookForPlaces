# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popular', '0011_auto_20150302_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailplaces',
            name='id',
        ),
        migrations.RemoveField(
            model_name='detailplaces',
            name='nq',
        ),
        migrations.AddField(
            model_name='detailplaces',
            name='place',
            field=models.OneToOneField(primary_key=True, default=1, serialize=False, to='popular.Places'),
            preserve_default=False,
        ),
    ]
