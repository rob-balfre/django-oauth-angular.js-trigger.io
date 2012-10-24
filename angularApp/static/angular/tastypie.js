angular.module('tastypieModule', ['ngResource']).
    factory('FoodOptions', function($resource, $timeout) {
        // if using django runsever locally be aware angular stips out the :
        // try using sudo with port 80 (OSX default port) which removes the need for using it
        var FoodOptions = $resource('http://192.168.91.20/api/:type',
            {type: 'food'},
            {
                get: {method: 'JSONP', params: {format: 'jsonp', callback:'JSON_CALLBACK'}},
                update: {method: 'POST', headers: {'Content-Type': 'application/json'}}
            }
        );
        
     return FoodOptions;
});