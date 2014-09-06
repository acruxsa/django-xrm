# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IdentificationType'
        db.create_table(u'core_identificationtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=127)),
        ))
        db.send_create_signal(u'core', ['IdentificationType'])

        # Adding model 'Person'
        db.create_table(u'core_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('identification_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.IdentificationType'])),
            ('identification', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('imagen_perfil', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Person'])

        # Adding model 'Contact'
        db.create_table(u'core_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_email', self.gf('django.db.models.fields.BooleanField')()),
            ('is_phone', self.gf('django.db.models.fields.BooleanField')()),
            ('is_sms', self.gf('django.db.models.fields.BooleanField')()),
            ('is_geo', self.gf('django.db.models.fields.BooleanField')()),
            ('is_skype', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'core', ['Contact'])

        # Adding model 'PersonContact'
        db.create_table(u'core_personcontact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contacts', to=orm['core.Contact'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Person'])),
        ))
        db.send_create_signal(u'core', ['PersonContact'])


    def backwards(self, orm):
        # Deleting model 'IdentificationType'
        db.delete_table(u'core_identificationtype')

        # Deleting model 'Person'
        db.delete_table(u'core_person')

        # Deleting model 'Contact'
        db.delete_table(u'core_contact')

        # Deleting model 'PersonContact'
        db.delete_table(u'core_personcontact')


    models = {
        u'core.contact': {
            'Meta': {'object_name': 'Contact'},
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_email': ('django.db.models.fields.BooleanField', [], {}),
            'is_geo': ('django.db.models.fields.BooleanField', [], {}),
            'is_phone': ('django.db.models.fields.BooleanField', [], {}),
            'is_skype': ('django.db.models.fields.BooleanField', [], {}),
            'is_sms': ('django.db.models.fields.BooleanField', [], {}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.identificationtype': {
            'Meta': {'object_name': 'IdentificationType'},
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        u'core.person': {
            'Meta': {'object_name': 'Person'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'identification_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.IdentificationType']"}),
            'imagen_perfil': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'core.personcontact': {
            'Meta': {'object_name': 'PersonContact'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': u"orm['core.Contact']"}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Person']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['core']
