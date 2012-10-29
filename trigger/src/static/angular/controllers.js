'use strict';

var loggedUser, apiKey;

function HomeCrtl($scope, $location) {
    //check for connecton 
    var online = navigator.onLine;
    
    //if connected attempt to login
    if (online === true) {
        $location.path('/sign-in');
    
    //else show connection error
    } else {
        $location.path('/no-connection');
    }
};

function SiginInCtrl($scope, $location, apiCall) {
    $scope.twitterSignIn = function() {
        //forge.tabs.openWithOptions({
          //  url: 'http://192.168.91.20/accounts/twitter/login/',
        //    pattern: 'http://192.168.91.20/auth/*'
        //}, function (data) {
            //forge.logging.log(data.url);
            //$scope.$apply(function() {
                $location.path('/list');
                loggedUser = 'rob_balfre';
                apiKey = '58ce21171b76da7755a7353313160867aeda1311';
            //});
        //}); 
    }
};

function ListCtrl($scope, $http, $location, apiCall) {
    console.log(loggedUser);
    $scope.food_options =  apiCall.get({username: loggedUser});
    
    $scope.testApi = function () {
        apiCall.get({username: loggedUser});
    }
    
    $scope.addNew = function() {
        $location.path('/new');
    }
};

function CreateCtrl($scope, $http, apiCall){
    $scope.addOption = function() {
        apiCall.post({username: loggedUser}, {'name':$scope.optionText});
    }
}