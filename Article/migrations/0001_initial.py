# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('group', models.CharField(max_length=32)),
                ('instime', models.DateTimeField(auto_now=True)),
                ('uptime', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('tags', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
