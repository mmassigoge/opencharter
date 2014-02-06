# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vehiculo'
        db.create_table(u'reservas_vehiculo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('patente', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('marca', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('modelo', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('anio', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('capacidad', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'reservas', ['Vehiculo'])

        # Adding model 'Chofer'
        db.create_table(u'reservas_chofer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dni', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('licencia', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('vencimiento', self.gf('django.db.models.fields.DateField')(null=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal(u'reservas', ['Chofer'])

        # Adding model 'Viaje'
        db.create_table(u'reservas_viaje', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_hora', self.gf('django.db.models.fields.DateTimeField')(unique=True)),
            ('vehiculo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reservas.Vehiculo'])),
            ('chofer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reservas.Chofer'])),
            ('ocupados', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'reservas', ['Viaje'])

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

        # Adding model 'Reserva'
        db.create_table(u'reservas_reserva', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pasajero', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reservas.Pasajero'])),
            ('viaje', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reservas.Viaje'])),
        ))
        db.send_create_signal(u'reservas', ['Reserva'])


    def backwards(self, orm):
        # Deleting model 'Vehiculo'
        db.delete_table(u'reservas_vehiculo')

        # Deleting model 'Chofer'
        db.delete_table(u'reservas_chofer')

        # Deleting model 'Viaje'
        db.delete_table(u'reservas_viaje')

        # Deleting model 'Pasajero'
        db.delete_table(u'reservas_pasajero')

        # Deleting model 'Reserva'
        db.delete_table(u'reservas_reserva')


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