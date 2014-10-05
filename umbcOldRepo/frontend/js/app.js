'use strict';
var includes = [
    'ngRoute',
    'ngCookies',
    'ui.ace',
    'angularProject.services',
    'angularProject.directives',
    'angularProject.controllers',
    ]

angular.module('angularProject', includes).
config(['$routeProvider','$httpProvider', function($routeProvider,$httpProvider) {
    $routeProvider.when('/', {templateUrl: 'partials/leaderboard.html', controller: 'leaderboard'});
    $routeProvider.when('/account', {templateUrl: 'partials/account.html', controller: 'account'});
    $routeProvider.when('/match', {templateUrl: 'partials/match.html', controller: 'match'});
    $routeProvider.when('/match/search', {templateUrl: 'partials/finding_match.html', controller: 'finding_match'});
    $routeProvider.when('/signin', {templateUrl: 'partials/signin.html', controller: 'signin'});
    $routeProvider.otherwise({redirectTo: '/'});
}])
.run(function($cookieStore, $rootScope, $http,$location) {
    if ($cookieStore.get('token')) {
        $http.defaults.headers.common['Authorization'] = 'Token ' + $cookieStore.get('token');
    }
})
.run(function($cookieStore,$rootScope, $location,$route) {
    $rootScope.$on( "$routeChangeStart", function(event, next, current) {
        if (!$cookieStore.get('token')) {
            if($location.path() != '/signin'){
                $location.path("/signin");
                //$route.reload();
            }
        }
    })
})