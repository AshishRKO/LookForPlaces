# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popular', '0002_auto_20150304_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailplaces',
            name='image2',
            field=models.ImageField(default=b'none', upload_to=b'detailplaces'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detailplaces',
            name='image3',
            field=models.ImageField(default=b'none', upload_to=b'detailplaces'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detailplaces',
            name='image4',
            field=models.ImageField(default=b'none', upload_to=b'detailplaces'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detailplaces',
            name='image5',
            field=models.ImageField(default=b'none', upload_to=b'detailplaces'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detailplaces',
            name='image6',
            field=models.ImageField(default=b'none', upload_to=b'detailplaces'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detailplaces',
            name='image7',
            field=models.ImageField(default=b'none', upload_to=b'detailplaces'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detailplaces',
            name='image8',
            field=models.ImageField(default=b'none', upload_to=b'detailplaces'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='detailplaces',
            name='image1',
            field=models.ImageField(default=b'none', upload_to=b'detailplaces'),
            preserve_default=True,
        ),
    ]
