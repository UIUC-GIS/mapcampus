function MapCtrl($scope, Buildings, Routes, GoogleMaps) {
  $scope.map = GoogleMaps;
  $scope.path = null;

  $scope.search = function(from, to) {
    var payload = Routes.get({from_id: from, to_id: to}, function() {
      if ($scope.path != null) {
        $scope.path.setMap(null);
      }

      var arr = $.map(payload.objects, function(obj) { 
        var coords = obj.coordinates.coordinates; 
        return new google.maps.LatLng(coords[1], coords[0]);
      });

      $scope.path = new google.maps.Polyline({
        path: arr,
        strokeColor: "#FF0000",
        strokeOpacity: 0.8,
        strokeWeight: 5
      });
      $scope.path.setMap($scope.map);

      var bounds = new google.maps.LatLngBounds();
      $scope.path.getPath().forEach(function(ll) {
        bounds.extend(ll);
      });
      $scope.map.panTo(bounds.getCenter());             
    });
  }
}