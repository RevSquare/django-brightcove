# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BrightcoveItems'
        db.create_table(u'django_brightcove_brightcoveitems', (
            ('brightcove_id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('video_still_URL', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('thumbnail_URL', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('short_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('long_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('length', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_URL', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('plays_total', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('published_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'django_brightcove', ['BrightcoveItems'])


    def backwards(self, orm):
        # Deleting model 'BrightcoveItems'
        db.delete_table(u'django_brightcove_brightcoveitems')


    models = {
        u'django_brightcove.brightcoveitems': {
            'Meta': {'object_name': 'BrightcoveItems'},
            'brightcove_id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'link_URL': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'long_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'plays_total': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'published_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'thumbnail_URL': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'video_still_URL': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['django_brightcove']