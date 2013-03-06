import networkx as nx

from tastypie import fields
from tastypie.resources import Resource
from tastypie.contrib.gis.resources import ModelResource

from apps.map.graph import LazyGraph
from apps.map.models import Building, Node, Edge

class DummyPaginator(object):
  def __init__(self, objects, collection_name='objects', **kwargs):
    self.objects = objects
    self.collection_name = collection_name

  def page(self):
    return {
      self.collection_name: self.objects,
    }

class BuildingResource(ModelResource):
  class Meta:
    queryset = Building.objects.all()
    resource_name = 'building'

class NodeResource(ModelResource):
  class Meta:
    resource_name = 'node'
    allowed_methods = ['get']
    object_class = Node
    #authentication = DjangoAuthentication()
    #filtering = { "pk": ['in', 'exact'], }

  def obj_get_list(self, bundle, **kwargs):
    lz = LazyGraph()
    return lz.get_node_dict().values()

class EdgeResource(ModelResource):
  node_src = fields.ToOneField(NodeResource, 'node_src', full=True)
  node_sink = fields.ToOneField(NodeResource, 'node_sink', full=True)
  
  class Meta:
    resource_name = 'edge'
    allowed_methods = ['get']
    object_class = Edge
    #authentication = DjangoAuthentication()
    #filtering = { "pk": ['in', 'exact'], }

  def obj_get_list(self, bundle, **kwargs):
    lz = LazyGraph()
    nd = lz.get_node_dict()
    edges = [edge for edge in Edge.objects.all()]
    for edge in edges:
      edge.node_src = nd[edge.node_src_id]
      edge.node_sink = nd[edge.node_sink_id]
    
    return edges

class RouteResource(ModelResource):
  class Meta:
    resource_name = 'route'
    allowed_methods = ['get']
    object_class = Node
    #authentication = DjangoAuthentication()
    #filtering = { "pk": ['in', 'exact'], }

  def obj_get_list(self, bundle, **kwargs):
    from_id = int(bundle.request.GET.get('from_id', -1))
    to_id = int(bundle.request.GET.get('to_id', -1))

    if from_id != -1 and to_id != -1:
      from_building = Building.objects.get(id=from_id)
      to_building = Building.objects.get(id=to_id)

      node_from_id = Node.objects.filter(building=from_building)[0].id
      node_to_id = Node.objects.filter(building=to_building)[0].id

      lz = LazyGraph()
      nd = lz.get_node_dict()
      length, path = nx.bidirectional_dijkstra(lz.get_graph(), from_id, to_id, weight='weight')

      return [nd[x] for x in path]

    return []

