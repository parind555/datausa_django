# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(unique=True, max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request_id', models.UUIDField(unique=True, null=True, blank=True)),
                ('update_time', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.CharField(default=b'Request received', max_length=50, choices=[(b'Request received', b'Request received'), (b'Request sent to datausa', b'Request sent to datausa'), (b'Answer received from datausa', b'Answer received from datausa'), (b'Error', b'Error'), (b'Answer to request delivered to the user', b'Answer to request delivered to the user')])),
                ('data', models.TextField()),
                ('user', models.ForeignKey(to='core.User')),
            ],
        ),
    ]
