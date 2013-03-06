// Generic init code
$(window).load(function() {
  // Fade in the entry box
  $("#entry").fadeIn();
});

'use strict'

// AngularJS stuff
angular.module('mc', ['mcServices'])
  .config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
  })
  .directive('buildingTypeahead', function(Buildings) {
  return {
    require: 'ngModel',
    restrict: 'A',

    link: function(scope, element, attrs, model) {  
      element.typeahead({
        source: function(query, process) {
          var payload = Buildings.get(function() {
            scope.building_map = {};
            var list = $.map(payload.objects, function(obj) { 
              scope.building_map[obj.name] = obj.id;
              return obj.name; 
            });

            return process(list);
          });
        }, 
        updater: function(item) {
          model.$setViewValue(scope.building_map[item]);
          return item;
        }
      });        
    }
  };
});