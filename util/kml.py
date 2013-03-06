#!/usr/bin/env python
import sys
import os
import traceback
import argparse

os.environ['DJANGO_SETTINGS_MODULE'] = "mapcampus.settings"

from django.contrib.gis.geos import Point
from lxml import etree

from apps.map.models import Node, Edge, Building

def parse_lines(fe):
  edges = []

  root = etree.parse(fe)
  lines = root.xpath("//line")
  for line in lines:
    from_name = line.xpath("./from")[0].text
    to_name = line.xpath("./to")[0].text

    edges.append((from_name, to_name))

  return edges

def parse_nodes(fn, ns):
  buildings = []
  nodes = {}

  root = etree.parse(fn)
  folders = root.xpath("//kml:Folder[kml:Placemark]", namespaces=ns)
  for folder in folders:
    building_name = folder.xpath("./kml:name", namespaces=ns)[0].text
    placemarks = folder.xpath("./kml:Placemark", namespaces=ns)

    building = Building(name=building_name)
    buildings.append(building)

    for placemark in placemarks:
      node_name = placemark.xpath("./kml:name", namespaces=ns)[0].text
      coordinates = placemark.xpath(".//kml:coordinates", namespaces=ns)[0].text
      frags = coordinates.split(',')
      
      lat, lng = frags[1], frags[0]

      nodes["{0}:{1}".format(building_name, node_name)] = \
        Node(coordinates=Point(x=float(lng), y=float(lat)), building=building)

  return buildings, nodes


def main():
  ns = {'kml': "http://www.opengis.net/kml/2.2"}
  with open(global_args.node_file) as fn, open(global_args.edge_file) as fe:
    buildings, nodes = parse_nodes(fn, ns)
    edges = parse_lines(fe)

  for building in buildings:
    building.save()

  for name in nodes:
    node = nodes[name]
    
    # get saved building
    saved_building = Building.objects.get(name=node.building.name)
    node.building = saved_building

    nodes[name].save()

    # update node in dictionary
    nodes[name] = node

  for (src, sink) in edges:
    node_src = nodes[src]
    node_sink = nodes[sink]
    edge = Edge(node_src=node_src, node_sink=node_sink, line=LineString(node_src.coordinates, node_sink.coordinates))
    edge.undirected_save()         

  return 0

if __name__ == '__main__':
  try:
    parser = argparse.ArgumentParser()
    parser.add_argument("node_file")
    parser.add_argument("edge_file")

    global_args = parser.parse_args()
    sys.exit(main())
  except KeyboardInterrupt, e: # Ctrl-C
    raise e
  except SystemExit, e: # sys.exit()
    raise e
  except Exception, e:
    print str(e)
    traceback.print_exc()
    exit(1)
