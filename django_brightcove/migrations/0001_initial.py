# -*- coding: utf-8 -*-
"""
This package is for Django migrations. South migrations can be found in the `south_migrations`
package.
"""
from __future__ import unicode_literals

SOUTH_ERROR_MESSAGE = """\n
To enable South migrations for this app customize the `SOUTH_MIGRATION_MODULES` setting in your
settings file such as the following:

    SOUTH_MIGRATION_MODULES = {
        'django_brightcove': 'django_brightcove.south_migrations',
    }
"""

try:
    from django.db import models, migrations
except ImportError:
    from django.core.exceptions import ImproperlyConfigured
    raise ImproperlyConfigured(SOUTH_ERROR_MESSAGE)


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrightcoveItems',
            fields=[
                ('brightcove_id', models.BigIntegerField(serialize=False, verbose_name='Brightcove id', primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name', blank=True)),
                ('video_still_URL', models.CharField(max_length=255, null=True, verbose_name='Video still url', blank=True)),
                ('thumbnail_URL', models.CharField(max_length=255, null=True, verbose_name='Thumbnail url', blank=True)),
                ('short_description', models.TextField(null=True, verbose_name='Short description', blank=True)),
                ('long_description', models.TextField(null=True, verbose_name='Short description', blank=True)),
                ('length', models.IntegerField(null=True, verbose_name='Length', blank=True)),
                ('link_URL', models.CharField(max_length=255, null=True, verbose_name='Link url', blank=True)),
                ('plays_total', models.PositiveIntegerField(null=True, verbose_name='Number of plays', blank=True)),
                ('creation_date', models.DateTimeField(null=True, verbose_name='Creation date', blank=True)),
                ('published_date', models.DateTimeField(null=True, verbose_name='Published date', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
