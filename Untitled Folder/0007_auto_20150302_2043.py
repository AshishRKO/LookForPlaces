# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popular', '0006_auto_20150302_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailplaces',
            name='image1',
            field=models.ImageField(upload_to=b'/detailplaces/'),
            preserve_default=True,
        ),
    ]
