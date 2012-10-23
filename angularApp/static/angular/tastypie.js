angular.module('tastypieModule', ['ngResource']).
    factory('FoodOptions', function($resource) {
        var FoodOptions = $resource('http://192.168.91.20/api/:type',
        {type: 'food', format: 'json'},
        {query: {method: 'JSONP'}}
        );
        
        console.log(FoodOptions);
        
    return FoodOptions;
});