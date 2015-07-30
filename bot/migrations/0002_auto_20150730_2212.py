# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='response',
        ),
        migrations.AddField(
            model_name='response',
            name='message',
            field=models.ForeignKey(to='bot.Message'),
        ),
        migrations.AddField(
            model_name='response',
            name='reply_to',
            field=models.ForeignKey(related_name='reply_to', to='bot.Message'),
        ),
        migrations.AlterUniqueTogether(
            name='response',
            unique_together=set([('message', 'reply_to')]),
        ),
    ]
