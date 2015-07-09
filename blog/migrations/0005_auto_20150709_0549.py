# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150709_0533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogspost',
            name='body_markdown',
        ),
        migrations.AlterField(
            model_name='blogspost',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogspost',
            name='timestamp',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='blogspost',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
