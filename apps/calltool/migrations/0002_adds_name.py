# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PhoneNumber.name'
        db.add_column('calltool_phonenumber', 'name',
                      self.gf('django.db.models.fields.CharField')(default='FOO', max_length=128),
                      keep_default=False)


        # Changing field 'PhoneNumber.extension'
        db.alter_column('calltool_phonenumber', 'extension', self.gf('django.db.models.fields.CharField')(max_length=32))

    def backwards(self, orm):
        # Deleting field 'PhoneNumber.name'
        db.delete_column('calltool_phonenumber', 'name')


        # Changing field 'PhoneNumber.extension'
        db.alter_column('calltool_phonenumber', 'extension', self.gf('django.db.models.fields.CharField')(max_length=34))

    models = {
        'calltool.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber'},
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'number': ('django.db.models.fields.IntegerField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['calltool']