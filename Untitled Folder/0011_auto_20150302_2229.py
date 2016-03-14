# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popular', '0010_auto_20150302_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailplaces',
            name='ids',
        ),
        migrations.RemoveField(
            model_name='places',
            name='ids',
        ),
        migrations.AddField(
            model_name='detailplaces',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detailplaces',
            name='nq',
            field=models.ForeignKey(default=1, to='popular.Places'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='places',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
