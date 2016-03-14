# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailPlaces',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=5000)),
                ('image1', models.ImageField(upload_to=b'detailplaces')),
                ('image2', models.ImageField(upload_to=b'detailplaces')),
                ('image3', models.ImageField(upload_to=b'detailplaces')),
                ('image4', models.ImageField(upload_to=b'detailplaces')),
                ('image5', models.ImageField(upload_to=b'detailplaces')),
                ('image6', models.ImageField(upload_to=b'detailplaces')),
                ('image7', models.ImageField(upload_to=b'detailplaces')),
                ('image8', models.ImageField(upload_to=b'detailplaces')),
                ('route', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=5000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
