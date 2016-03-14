# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popular', '0003_auto_20150221_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailplaces',
            name='image1',
            field=models.ImageField(default='none', upload_to=b''),
            preserve_default=False,
        ),
    ]
