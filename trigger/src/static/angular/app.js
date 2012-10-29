'use strict';

var app = angular.module('fff', ['tastypieModule'])
    .config(function($routeProvider) { $routeProvider.
        when('/', {controller:HomeCrtl, templateUrl:'partials/home.html'}).
        when('/sign-in', {controller:SiginInCtrl, templateUrl:'partials/sign-in.html'}).
        when('/no-connection', {templateUrl:'partials/no-connection.html'}).
        when('/list', {controller:ListCtrl, templateUrl:'partials/list.html'}).
        when('/new', {controller:CreateCtrl, templateUrl:'partials/add_option.html'}).
        otherwise({redirectTo:'/'});
    })
    .run( function($rootScope, $location) {
        $rootScope.$on( "$routeChangeStart", function(event, next, current) {
            if ( $rootScope.loggedUser == null ) {
                // no logged user, we should be going to #login
                if ( next.templateUrl == "partials/login.html" ) {
                    // already going to #login, no redirect needed
                } else {
                    // not going to #login, we should redirect now
                    $location.path( "/login" );
                }
            }
        });
    }
    
