'use strict';

angular.module('mcServices', ['ngResource'])
  .factory('Buildings', function($resource) {
    return $resource(
      '/api/v1/building/', 
      { format: 'json' }, 
      { query: {method: 'GET', isArray: true } }
    );
  })
  .factory('Nodes', function($resource) {
    return $resource(
      '/api/v1/node/', 
      { format: 'json' }, 
      { query: {method: 'GET', isArray: true } }
    );
  })
  .factory('Routes', function($resource) {
    return $resource(
      '/api/v1/route/', 
      { format: 'json' }, 
      { query: {method: 'GET', isArray: true } }
    );
  })
  .factory('GoogleMaps', function() {
    var map = new google.maps.Map(
      $("#map_canvas")[0], 
      {
        center: new google.maps.LatLng(40.10804, -88.22726),
        zoom: 18,
        mapTypeId: google.maps.MapTypeId.ROADMAP
      }
    );
    // Resize the window accordingly
    var wnd = $(window);
    var center = $("#center");
    var top = $("#north").height();

    wnd.resize(function() {
      center.height(wnd.height() - top);
    });
    wnd.trigger("resize");

    return map;
  });