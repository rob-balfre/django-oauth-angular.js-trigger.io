'use strict';

function getURLParameter(name, url) {
    console.log(name);
    return decodeURI(
        (RegExp(name + '=' + '(.+?)(&|$)').exec(url)||[,null])[1]
    );
}

app.controller('MainAppCtrl', function($scope, $rootScope, $location, apiCall) {
    $rootScope.$on('event:auth-loginRequired', function(){
          $location.path('/');
    });
    
    $scope.twitterAvatar = apiCall.get({type: 'avatar', username: localStorage.getItem("username"), api_key: localStorage.getItem("apiKey"), user: localStorage.getItem("userID")});

});

function HomeCrtl($scope, $location) {
    //check for connecton 
    var online = navigator.onLine;
    
    //if connected attempt to login
    if (online === true) {
        $location.path('/user');
    
    //else show connection error
    } else {
        $location.path('/no-connection');
    }
};
//HomeCrtl.$inject = [];


function SiginInCtrl($scope, $location, apiCall) {
    $scope.twitterSignIn = function() {
        forge.tabs.openWithOptions({
            url: 'http://192.168.91.20/accounts/twitter/login/',
            pattern: 'http://192.168.91.20/auth/*'
            }, function (data) {
            forge.logging.log(data.url);
            $scope.$apply(function() {
                //var theURL = 'http://192.168.91.20/auth/?username=lolcharr&api_key=f94bb5bf3f6a7e645c4191f749fd930c2a8f2f85&user=3';
                var theURL = data.url;
                localStorage.setItem("userID", getURLParameter('user', theURL));
                localStorage.setItem("username", getURLParameter('username', theURL));
                localStorage.setItem("apiKey", getURLParameter('api_key', theURL));
                $location.path('/list');

            });
        }); 
    }
};

function ListCtrl($rootScope, $scope, $location, apiCall) {
    function getFoodOptions() {
        $scope.food_options =  apiCall.get({type: 'food', username: localStorage.getItem("username"), api_key: localStorage.getItem("apiKey")});
        $scope.current_vote = apiCall.get({type: 'vote', username: localStorage.getItem("username"), api_key: localStorage.getItem("apiKey"), user: localStorage.getItem("userID")});
    }
        
    getFoodOptions();

    
    $scope.testApi = function () {
        $scope.food_options = apiCall.get({type: 'food', username: localStorage.getItem("username"), api_key: localStorage.getItem("apiKey")});
    }
    
    $scope.addNew = function() {
        $location.path('/new');
    }
    
    $scope.attemptVote = function () {
        apiCall.post(
            {type: 'vote', username: localStorage.getItem("username"), api_key: localStorage.getItem("apiKey")}, 
            {'food_option': {'id': this.food_option.id }, 'user': {'username': localStorage.getItem("username")}}, 
            function() {
                getFoodOptions();
            });
    };
    
    $scope.refresh = function () {
        getFoodOptions();
    }
    
};

function CreateCtrl($scope, $location, apiCall){
    $scope.food_options =  apiCall.get({type: 'food', username: localStorage.getItem("username"), api_key: localStorage.getItem("apiKey")});
    
    $scope.addOption = function() {
        apiCall.post(
            {type: 'food', username: localStorage.getItem("username"), api_key: localStorage.getItem("apiKey"),  user: localStorage.getItem("userID")},
            {'name': $scope.optionText, 'votes': 0 }, 
        function() {
                $location.path('/list');
            });
    }
}