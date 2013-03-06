import networkx as nx
from django.db import connection, transaction
from models import Edge, Node

class LazyGraph(object):
  _graph = None
  _node_dict = {};

  def get_graph(self):
    if not LazyGraph._graph:
      LazyGraph._graph = nx.Graph()

      cursor = connection.cursor()
      cursor.execute("SELECT id, node_src_id, node_sink_id, weight FROM map_edge")
      for row in cursor.fetchall():
        LazyGraph._graph.add_edge(
          row[1], 
          row[2], 
          { 'weight': row[3] }
        )
        
    return LazyGraph._graph

  def get_node_dict(self):
    if not LazyGraph._node_dict:
      for node in Node.objects.all():
        LazyGraph._node_dict[node.id] = node

    return LazyGraph._node_dict