# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popular', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailplaces',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='detailplaces',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='detailplaces',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='detailplaces',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='detailplaces',
            name='image6',
        ),
        migrations.RemoveField(
            model_name='detailplaces',
            name='image7',
        ),
        migrations.RemoveField(
            model_name='detailplaces',
            name='image8',
        ),
    ]
