from django.db import models
from django.contrib.gis.db import models as gmodels
from django.contrib import admin
from apps.admin.options import GoogleMapsAdmin 

class Building(gmodels.Model):
  name = models.CharField(max_length=100)

class Node(gmodels.Model):
  coordinates = gmodels.PointField(null=False)
  building = gmodels.ForeignKey(Building)
  objects = gmodels.GeoManager()

class Edge(gmodels.Model):
  node_src = gmodels.ForeignKey(Node, related_name='edge_node_src')
  node_sink = gmodels.ForeignKey(Node, related_name='edge_node_sink')
  objects = gmodels.GeoManager()

  def undirected_save(self):
    Edge.objects.get_or_create(node_src=self.node_sink, node_sink=self.node_src)
    self.save()

admin.site.register(Node, GoogleMapsAdmin)
admin.site.register(Edge, GoogleMapsAdmin)
