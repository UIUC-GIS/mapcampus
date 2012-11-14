from django.contrib.gis.admin import GeoModelAdmin

class GoogleMapsModelAdmin(GeoModelAdmin):
    map_template = 'gis/admin/openlayers.html'
    openlayers_url = 'http://openlayers.org/api/OpenLayers.js'
