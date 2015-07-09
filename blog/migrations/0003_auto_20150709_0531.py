# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150709_0529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name=b'Title')),
                ('timestamp', models.DateTimeField(verbose_name=b'Date published')),
                ('body_markdown', models.TextField(help_text=b'Use Markdown syntax.', verbose_name=b'Entry body')),
                ('body', models.TextField(null=True, verbose_name=b'Entry body as HTML', blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='BlogsPost',
        ),
    ]
