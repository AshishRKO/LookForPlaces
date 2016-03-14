# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popular', '0012_auto_20150302_2235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detailplaces',
            old_name='place',
            new_name='id',
        ),
    ]
