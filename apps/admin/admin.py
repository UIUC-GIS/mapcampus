from django.forms import ModelChoiceField
from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from apps.map.models import Building, Node, Edge

class BuildingAdmin(admin.ModelAdmin):  
  list_display = ['name']

class NodeBuildingChoiceField(ModelChoiceField):
  def label_from_instance(self, obj):
    return obj.name

class NodeAdmin(OSMGeoAdmin):
  list_display = ['coordinates']

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == "building":
      kwargs["queryset"] = Building.objects.all()
      return NodeBuildingChoiceField(**kwargs)
    return super(NodeAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class EdgeNodeChoiceField(ModelChoiceField):
  def label_from_instance(self, obj):
    return obj.coordinates

class EdgeAdmin(OSMGeoAdmin):
  list_display = ['node_src_display', 'node_sink_display']

  def node_src_display(self, obj):
    return obj.node_src.coordinates

  def node_sink_display(self, obj):
    return obj.node_sink.coordinates

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == "node_src" or db_field.name == "node_sink":
      kwargs["queryset"] = Node.objects.all()
      return EdgeNodeChoiceField(**kwargs)
    return super(EdgeAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  node_src_display.short_description = 'Node source'
  node_sink_display.short_description = 'Node sink'

admin.site.register(Building, BuildingAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(Edge, EdgeAdmin)