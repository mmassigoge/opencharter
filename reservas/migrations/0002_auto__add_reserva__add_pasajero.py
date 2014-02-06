# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Reserva'
        db.create_table(u'reservas_reserva', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pasajero', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reservas.Pasajero'])),
            ('viaje', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reservas.Viaje'])),
        ))
        db.send_create_signal(u'reservas', ['Reserva'])

        # Adding model 'Pasajero'
        db.create_table(u'reservas_pasajero', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dni', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254)),
            ('clave', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal(u'reservas', ['Pasajero'])


    def backwards(self, orm):
        # Deleting model 'Reserva'
        db.delete_table(u'reservas_reserva')

        # Deleting model 'Pasajero'
        db.delete_table(u'reservas_pasajero')


    models = {
        u'reservas.chofer': {
            'Meta': {'object_name': 'Chofer'},
            'dni': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'licencia': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'vencimiento': ('django.db.models.fields.DateField', [], {'null': 'True'})
        },
        u'reservas.pasajero': {
            'Meta': {'object_name': 'Pasajero'},
            'clave': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dni': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'reservas.reserva': {
            'Meta': {'object_name': 'Reserva'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pasajero': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reservas.Pasajero']"}),
            'viaje': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reservas.Viaje']"})
        },
        u'reservas.vehiculo': {
            'Meta': {'object_name': 'Vehiculo'},
            'anio': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'capacidad': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'modelo': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'patente': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'})
        },
        u'reservas.viaje': {
            'Meta': {'object_name': 'Viaje'},
            'chofer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reservas.Chofer']"}),
            'fecha_hora': ('django.db.models.fields.DateTimeField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ocupados': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'vehiculo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reservas.Vehiculo']"})
        }
    }

    complete_apps = ['reservas']