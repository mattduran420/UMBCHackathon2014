angular.module('angularProject.directives',[])

.value("baseURL","http://localhost:8000/")


/* google says this makes my links change based on route */
/* confirmed working */
.directive('activeLink', ['$location', function(location) {
    return {
      restrict: 'A',
      link: function(scope, element, attrs, controller) {
        var clazz = attrs.activeLink;
        var path = attrs.href;
        path = $(element).children("a")[0].hash.substring(1);
        scope.location = location;
        scope.$watch('location.path()', function(newPath) {
          if (path === newPath) {
            element.addClass(clazz);
          } else {
            element.removeClass(clazz);
          }
        });
      }
    };
  }])
