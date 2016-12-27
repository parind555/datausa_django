# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userrequest',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='request_id',
            field=models.UUIDField(serialize=False, primary_key=True, blank=True),
        ),
    ]
