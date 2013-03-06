#!/usr/bin/env python
import cProfile
import os
import networkx as nx

os.environ['DJANGO_SETTINGS_MODULE'] = "mapcampus.settings"

from apps.map.graph import LazyGraph
from apps.map.models import Node, Edge, Building

def foo():
  lz = LazyGraph()
  lz.get_graph()

cProfile.run('foo()', sort=1)