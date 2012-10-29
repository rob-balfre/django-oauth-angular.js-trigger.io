angular.module('tastypieModule', ['ngResource']).
    factory('apiCall', function($http, $resource) {
        // if using django runsever locally be aware angular stips out the :
        // try using sudo with port 80 (OSX default port) which removes the need for using it
        //$http.defaults.useXDomain = true;
        //$http.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        delete $http.defaults.headers.common['X-Requested-With'];
        
        var apiCall = $resource('http://192.168.91.20/api/:type',
            {type: 'food', username: 'rob_balfre', api_key: '58ce21171b76da7755a7353313160867aeda1311'},
            {
                get: {method: 'GET'},
                //update: {method: 'POST', params: { withCredentials: true, action: 'create', format: 'json' }, headers: {'Content-Type': 'application/json', 'dataType': 'application/json'}}
            }
        );
        
     return apiCall;
})


//  http://lit-hollows-9760.herokuapp.com/api/:type */

/*
angular.module('tastypieModule', ['ngResource']).
    factory('apiCall', function() {
        var apiCall = {
            get : function () {
                $.ajax({
                    type: 'GET',
                    url: 'http://192.168.91.20/api/food/?username=rob_balfre&api_key=58ce21171b76da7755a7353313160867aeda1311',
                    //data: '{"name":"'+$scope.optionText+'"}',
                    contentType: "application/json"
                    //dataType: 'json',
                    //processData: false
                }).done(function(data) { return apiCall });
            }
        }
        return apiCall;
    });
*/


