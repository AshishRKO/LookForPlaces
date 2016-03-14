# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popular', '0009_auto_20150302_2225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detailplaces',
            old_name='id',
            new_name='ids',
        ),
        migrations.RenameField(
            model_name='places',
            old_name='id',
            new_name='ids',
        ),
    ]
