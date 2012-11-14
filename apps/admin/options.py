from django.contrib.gis.admin import GeoModelAdmin

class GoogleMapsAdmin(GeoModelAdmin):
    map_template = 'google.html'
    openlayers_url = 'http://openlayers.org/api/OpenLayers.js'
    extra_js = ['http://maps.googleapis.com/maps/api/js?sensor=true&v=3.6']
