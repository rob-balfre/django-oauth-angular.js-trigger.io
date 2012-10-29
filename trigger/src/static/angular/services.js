'use strict';

angular.module('tastypieModule', ['ngResource']).
    factory('apiCall', function($http, $resource) {
        // if your using django tastypie as the API locally be aware angular stips out the : (for example locahost:8000 wont work)
        // try using sudo with port 80 (OSX's default port) which removes the need for using it
        delete $http.defaults.headers.common['X-Requested-With'];
        
        var apiCall = $resource('http://192.168.91.20/api/:type',
            {type: 'food', username: '@userName', api_key: '58ce21171b76da7755a7353313160867aeda1311'},
            {
                get: {method: 'GET'},
                post: {method: 'POST', headers: {'Content-Type': 'application/json'}}
            }
        );
        
     return apiCall;
})