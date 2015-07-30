# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('json', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateTimeField()),
                ('response', models.ForeignKey(to='bot.Message', null=True, related_name='response_id', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('update_id', models.CharField(primary_key=True, max_length='40', serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(to='bot.User'),
        ),
    ]
