from django.db import models
from django.contrib.gis.db import models as gismodels
from django.contrib import admin

class Building(models.Model):
  name = models.CharField(max_length=100)

class Node(gismodels.Model):
  coordinates = gismodels.PointField(null=False)
  building = gismodels.ForeignKey(Building, null=True, blank=True)
  objects = gismodels.GeoManager()

class Edge(gismodels.Model):
  node_src = gismodels.ForeignKey(Node, related_name='edge_node_src')
  node_sink = gismodels.ForeignKey(Node, related_name='edge_node_sink')
  weight = models.FloatField(default=0.0); 
  objects = gismodels.GeoManager()

  def undirected_save(self):
    Edge.objects.get_or_create(node_src=self.node_sink, node_sink=self.node_src)
    self.save()