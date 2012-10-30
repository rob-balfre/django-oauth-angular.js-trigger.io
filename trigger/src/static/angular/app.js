'use strict';

var app = angular.module('fff', ['http-auth-interceptor','tastypieModule'])
    .config(function($routeProvider) { $routeProvider.
        when('/', {controller:HomeCrtl, templateUrl:'partials/home.html'}).
        when('/sign-in', {controller:SiginInCtrl, templateUrl:'partials/sign-in.html'}).
        when('/no-connection', {templateUrl:'partials/no-connection.html'}).
        when('/list', {controller:ListCtrl, templateUrl:'partials/list.html'}).
        when('/new', {controller:CreateCtrl, templateUrl:'partials/add_option.html'}).
        otherwise({redirectTo:'/'});
    });

app.controller('MainAppCtrl', function($scope, $rootScope, $location) {
    $rootScope.$on('event:auth-loginRequired', function(){
          $location.path('/');
    });
});