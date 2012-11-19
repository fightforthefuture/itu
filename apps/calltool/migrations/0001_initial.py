# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PhoneNumber'
        db.create_table('calltool_phonenumber', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2)),
            ('number', self.gf('django.db.models.fields.IntegerField')(max_length=32)),
            ('extension', self.gf('django.db.models.fields.CharField')(max_length=34, blank=True)),
        ))
        db.send_create_signal('calltool', ['PhoneNumber'])


    def backwards(self, orm):
        # Deleting model 'PhoneNumber'
        db.delete_table('calltool_phonenumber')


    models = {
        'calltool.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber'},
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '34', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['calltool']