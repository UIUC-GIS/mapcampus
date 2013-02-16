#!/usr/bin/env python
import sys
import os
import traceback
import argparse

os.environ['DJANGO_SETTINGS_MODULE'] = "mapcampus.settings"

from django.contrib.gis.geos import Point
from lxml import etree

from apps.map.models import Node, Building

def main():
  ns = {'kml': "http://www.opengis.net/kml/2.2"}
  with open(global_args.node_file) as fn, open(global_args.edge_file) as fe:
    root = etree.parse(fn)
    folders = root.xpath("kml:Document/kml:Folder//kml:Folder", namespaces=ns)
    for folder in folders:
      name = folder.xpath("./kml:name", namespaces=ns)[0]
      coords = folder.xpath(".//kml:coordinates", namespaces=ns)

      b = Building(name=name.text)
      b.save()

      for coord in coords:
        frags = coord.text.split(',')
        lng = frags[0]
        lat = frags[1]
        
        n = Node(coordinates=Point(float(lat), float(lng)), building=b)
        n.save()
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
