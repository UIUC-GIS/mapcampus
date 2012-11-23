# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Building'
        db.create_table('map_building', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('map', ['Building'])

        # Adding model 'Node'
        db.create_table('map_node', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('coordinates', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('building', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['map.Building'])),
        ))
        db.send_create_signal('map', ['Node'])

        # Adding model 'Edge'
        db.create_table('map_edge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node_src', self.gf('django.db.models.fields.related.ForeignKey')(related_name='edge_node_src', to=orm['map.Node'])),
            ('node_sink', self.gf('django.db.models.fields.related.ForeignKey')(related_name='edge_node_sink', to=orm['map.Node'])),
        ))
        db.send_create_signal('map', ['Edge'])

    def backwards(self, orm):
        # Deleting model 'Building'
        db.delete_table('map_building')

        # Deleting model 'Node'
        db.delete_table('map_node')

        # Deleting model 'Edge'
        db.delete_table('map_edge')

    models = {
        'map.building': {
            'Meta': {'object_name': 'Building'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'map.edge': {
            'Meta': {'object_name': 'Edge'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node_sink': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'edge_node_sink'", 'to': "orm['map.Node']"}),
            'node_src': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'edge_node_src'", 'to': "orm['map.Node']"})
        },
        'map.node': {
            'Meta': {'object_name': 'Node'},
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['map.Building']"}),
            'coordinates': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['map']