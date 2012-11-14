from tastypie import fields
from tastypie.contrib.gis.resources import ModelResource

from apps.map.models import Node, Edge

class EdgeResource(ModelResource):
  class Meta:
    queryset = Edge.objects.all()
    resource_name = 'edge'

class NodeResource(ModelResource):
  class Meta:
    queryset = Node.objects.all()
    resource_name = 'node'