angular.module('tastypieModule', ['ngResource']).
    factory('FoodOptions', function($http, $resource) {
        // if using django runsever locally be aware angular stips out the :
        // try using sudo with port 80 (OSX default port) which removes the need for using it
        $http.defaults.useXDomain = true;
        
        var FoodOptions = $resource('http://192.168.91.20/api/:type',
            {type: 'food', username: 'testy', api_key: '32331180f4d70523597be5a027223a9cfaf90fdd'},
            {
                get: {method: 'JSONP', params: { format: 'jsonp', callback:'JSON_CALLBACK'}},
                //update: {method: 'POST', params: { withCredentials: true, action: 'create', format: 'json' }, headers: {'Content-Type': 'application/json', 'dataType': 'application/json'}}
            }
        );
        
     return FoodOptions;
});


//  http://lit-hollows-9760.herokuapp.com/api/:type