function EditCtrl($scope, Buildings, Nodes, Routes, GoogleMaps) {
  $scope.map = GoogleMaps;
  $scope.circles = null;

  $scope.getEdges = function() {
    if ($scope.circles != null) {
      $scope.circles.forEach(function(circle) {
        circle.setMap(null); 
      });
    }
    $scope.circles = [];

    var payload = Nodes.get({ limit: 2000 }, function() {
      payload.objects.forEach(function(obj) {
        var coords = obj.coordinates.coordinates; 
        var circle = new google.maps.Circle({
          strokeColor: "#FF0000",
          strokeOpacity: 0.8,
          strokeWeight: 2,
          fillColor: "#FF0000",
          fillOpacity: 0.35,
          center: new google.maps.LatLng(coords[1], coords[0]),
          radius: 2
        });
        circle.setMap($scope.map);
        $scope.circles.push(circle);
      });   
    });
  }
}