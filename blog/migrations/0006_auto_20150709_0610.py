# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150709_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogspost',
            name='body_markdown',
            field=models.TextField(default=datetime.datetime(2015, 7, 9, 6, 10, 8, 936510, tzinfo=utc), help_text=b'Use Markdown syntax.', verbose_name=b'Entry body'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogspost',
            name='body',
            field=models.TextField(null=True, blank=True),
        ),
    ]
