# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'IdentificationType.creado_el'
        db.delete_column(u'core_identificationtype', 'creado_el')

        # Deleting field 'IdentificationType.modificado_el'
        db.delete_column(u'core_identificationtype', 'modificado_el')

        # Adding field 'IdentificationType.created_at'
        db.add_column(u'core_identificationtype', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 9, 6, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'IdentificationType.modified_at'
        db.add_column(u'core_identificationtype', 'modified_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 9, 6, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'Person.modificado_el'
        db.delete_column(u'core_person', 'modificado_el')

        # Deleting field 'Person.creado_el'
        db.delete_column(u'core_person', 'creado_el')

        # Adding field 'Person.created_at'
        db.add_column(u'core_person', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 9, 6, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Person.modified_at'
        db.add_column(u'core_person', 'modified_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 9, 6, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'PersonContact.modificado_el'
        db.delete_column(u'core_personcontact', 'modificado_el')

        # Deleting field 'PersonContact.creado_el'
        db.delete_column(u'core_personcontact', 'creado_el')

        # Adding field 'PersonContact.created_at'
        db.add_column(u'core_personcontact', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 9, 6, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'PersonContact.modified_at'
        db.add_column(u'core_personcontact', 'modified_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 9, 6, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'Contact.creado_el'
        db.delete_column(u'core_contact', 'creado_el')

        # Deleting field 'Contact.modificado_el'
        db.delete_column(u'core_contact', 'modificado_el')

        # Adding field 'Contact.created_at'
        db.add_column(u'core_contact', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 9, 6, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Contact.modified_at'
        db.add_column(u'core_contact', 'modified_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 9, 6, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'IdentificationType.creado_el'
        db.add_column(u'core_identificationtype', 'creado_el',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 9, 6, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'IdentificationType.modificado_el'
        db.add_column(u'core_identificationtype', 'modificado_el',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 9, 6, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'IdentificationType.created_at'
        db.delete_column(u'core_identificationtype', 'created_at')

        # Deleting field 'IdentificationType.modified_at'
        db.delete_column(u'core_identificationtype', 'modified_at')

        # Adding field 'Person.modificado_el'
        db.add_column(u'core_person', 'modificado_el',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 9, 6, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Person.creado_el'
        db.add_column(u'core_person', 'creado_el',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 9, 6, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'Person.created_at'
        db.delete_column(u'core_person', 'created_at')

        # Deleting field 'Person.modified_at'
        db.delete_column(u'core_person', 'modified_at')

        # Adding field 'PersonContact.modificado_el'
        db.add_column(u'core_personcontact', 'modificado_el',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 9, 6, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'PersonContact.creado_el'
        db.add_column(u'core_personcontact', 'creado_el',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 9, 6, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'PersonContact.created_at'
        db.delete_column(u'core_personcontact', 'created_at')

        # Deleting field 'PersonContact.modified_at'
        db.delete_column(u'core_personcontact', 'modified_at')

        # Adding field 'Contact.creado_el'
        db.add_column(u'core_contact', 'creado_el',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 9, 6, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Contact.modificado_el'
        db.add_column(u'core_contact', 'modificado_el',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 9, 6, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'Contact.created_at'
        db.delete_column(u'core_contact', 'created_at')

        # Deleting field 'Contact.modified_at'
        db.delete_column(u'core_contact', 'modified_at')


    models = {
        u'core.contact': {
            'Meta': {'object_name': 'Contact'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_email': ('django.db.models.fields.BooleanField', [], {}),
            'is_geo': ('django.db.models.fields.BooleanField', [], {}),
            'is_phone': ('django.db.models.fields.BooleanField', [], {}),
            'is_skype': ('django.db.models.fields.BooleanField', [], {}),
            'is_sms': ('django.db.models.fields.BooleanField', [], {}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.identificationtype': {
            'Meta': {'object_name': 'IdentificationType'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        u'core.person': {
            'Meta': {'object_name': 'Person'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'identification_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.IdentificationType']"}),
            'imagen_perfil': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'core.personcontact': {
            'Meta': {'object_name': 'PersonContact'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': u"orm['core.Contact']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Person']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['core']
