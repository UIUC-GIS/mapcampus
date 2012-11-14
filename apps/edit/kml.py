from django.contrib.gis.geos import Point
from lxml import etree

from apps.map.models import Node, Building

def import_kml(f):
  def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

ns = {'kml': "http://www.opengis.net/kml/2.2"}
with open("../../../campus.kml") as f:
  root = etree.parse(f)
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
      
      n = Node(coordinates=Point(float(lat), float(lng))
      n.save()

#w