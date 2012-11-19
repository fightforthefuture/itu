# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'PhoneNumber.number'
        db.alter_column('calltool_phonenumber', 'number', self.gf('django.db.models.fields.CharField')(max_length=32))

    def backwards(self, orm):

        # Changing field 'PhoneNumber.number'
        db.alter_column('calltool_phonenumber', 'number', self.gf('django.db.models.fields.IntegerField')(max_length=32))

    models = {
        'calltool.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['calltool']