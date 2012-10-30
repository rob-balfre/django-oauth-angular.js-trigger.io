'use strict';

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
//HomeCrtl.$inject = [];


function SiginInCtrl($scope, $location, apiCall) {
    $scope.twitterSignIn = function() {
        //forge.tabs.openWithOptions({
          //  url: 'http://192.168.91.20/accounts/twitter/login/',
        //    pattern: 'http://192.168.91.20/auth/*'
        //}, function (data) {
            //forge.logging.log(data.url);
            //$scope.$apply(function() {
                $location.path('/list');
                localStorage.setItem("username", "rob_balfre");
                localStorage.setItem("apiKey", "58ce21171b76da7755a7353313160867aeda1311");
                
                //loggedUser = 'rob_balfre';
                //apiKey = '58ce21171b76da7755a7353313160867aeda1311';
            //});
        //}); 
    }
};

function ListCtrl($rootScope, $scope, $http, $location, apiCall) {
    $scope.food_options =  apiCall.get({username: localStorage.getItem("username")});
    
    $scope.testApi = function () {
        apiCall.get({username: localStorage.getItem("username"), api_key: localStorage.getItem("apiKey")});
    }
    
    $scope.addNew = function() {
        $location.path('/new');
    }
    
    $scope.sendVote = function (foodID) {
        apiCall.post({type: 'vote', username: localStorage.getItem("username"), api_key: localStorage.getItem("apiKey")}, {'food_option': {'id': foodID}, 'user': {'username': localStorage.getItem("username")}});
    }
    
};

function CreateCtrl($scope, $http, apiCall){
    $scope.addOption = function() {
        apiCall.post({username: loggedUser}, {'name':$scope.optionText});
    }
}