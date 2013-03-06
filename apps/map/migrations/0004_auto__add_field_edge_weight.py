# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Edge.weight'
        db.add_column(u'map_edge', 'weight',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Edge.weight'
        db.delete_column(u'map_edge', 'weight')

    models = {
        u'map.building': {
            'Meta': {'object_name': 'Building'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'map.edge': {
            'Meta': {'object_name': 'Edge'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node_sink': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'edge_node_sink'", 'to': u"orm['map.Node']"}),
            'node_src': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'edge_node_src'", 'to': u"orm['map.Node']"}),
            'weight': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        },
        u'map.node': {
            'Meta': {'object_name': 'Node'},
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['map.Building']", 'null': 'True', 'blank': 'True'}),
            'coordinates': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['map']