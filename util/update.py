#!/usr/bin/env python
import os

os.environ['DJANGO_SETTINGS_MODULE'] = "mapcampus.settings"

from apps.map.models import Node, Edge

for edge in Edge.objects.all():
  src = edge.node_src
  sink = edge.node_sink
  edge.weight = src.coordinates.distance(sink.coordinates) 
  edge.save()