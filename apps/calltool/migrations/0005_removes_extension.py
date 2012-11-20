# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PhoneNumber.extension'
        db.delete_column('calltool_phonenumber', 'extension')


    def backwards(self, orm):
        # Adding field 'PhoneNumber.extension'
        db.add_column('calltool_phonenumber', 'extension',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)


    models = {
        'calltool.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['calltool']