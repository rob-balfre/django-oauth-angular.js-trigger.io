'use strict';

function getURLParameter(name, url) {
  return decodeURI((RegExp(name + '=' + '(.+?)(&|$)').exec(url) || [, null])[1]);
}

app.controller('MainAppCtrl', function($scope, $rootScope, $location, apiCall) {
  $rootScope.$on('event:auth-loginRequired', function() {
    $location.path('/');
  });

  $scope.twitterAvatar = apiCall.get({
    type: 'avatar',
    username: localStorage.getItem("username"),
    api_key: localStorage.getItem("apiKey"),
    user: localStorage.getItem("userID")
  });
});

app.controller('tabCtrl', function($scope, $location) {
    $scope.isActive = function(route) {
        return route === $location.path();
    }
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

function SiginInCtrl($scope, $location, apiCall) {
  $scope.twitterSignIn = function() {
    var theURL;

    if (typeof forge === "undefined") {
      theURL = 'http://192.168.91.20/auth/?username=artitudinale&api_key=0ee2e04b1e4e5ec3e60d436194d3b37b9a3c0f14&user=6';
      setLocalStorage(theURL);
      $location.path('/list');
    } else {
      forge.tabs.openWithOptions({
        url: 'http://192.168.91.20/accounts/twitter/login/',
        pattern: 'http://192.168.91.20/auth/*'
      }, function(data) {
        forge.logging.log(data.url);
        
         $scope.$apply(function() {
           setLocalStorage(data.url);
           $location.path('/list');
        });
      });
    };
  };
};

function setLocalStorage(data) {
    localStorage.setItem("userID", getURLParameter('user', data));
    localStorage.setItem("username", getURLParameter('username', data));
    localStorage.setItem("apiKey", getURLParameter('api_key', data));  
};


function ListCtrl($rootScope, $scope, $location, apiCall) {
  function getFoodOptions() {
    $scope.food_options = apiCall.get({
      type: 'food',
      username: localStorage.getItem("username"),
      api_key: localStorage.getItem("apiKey")
    });
    
   // $scope.food_options = foodOptions;
    
    $scope.current_vote = apiCall.get({
      type: 'vote',
      username: localStorage.getItem("username"),
      api_key: localStorage.getItem("apiKey"),
      user: localStorage.getItem("userID")
    });
  }

  getFoodOptions();


  $scope.testApi = function() {
    $scope.food_options = apiCall.get({
      type: 'food',
      username: localStorage.getItem("username"),
      api_key: localStorage.getItem("apiKey")
    });
  }

  $scope.addNew = function() {
    $location.path('/new');
  }

  $scope.attemptVote = function() {
    apiCall.post({
      type: 'vote',
      username: localStorage.getItem("username"),
      api_key: localStorage.getItem("apiKey")
    }, {
      'food_option': {
        'id': this.food_option.id
      },
      'user': {
        'username': localStorage.getItem("username")
      }
    }, function() {
      getFoodOptions();
    });
  };

  $scope.refresh = function() {
    getFoodOptions();
  };
};

function CreateCtrl($scope, $location, apiCall) {
  $scope.food_options = apiCall.get({
    type: 'food',
    username: localStorage.getItem("username"),
    api_key: localStorage.getItem("apiKey")
  });

  $scope.addOption = function() {
    apiCall.post({
      type: 'food',
      username: localStorage.getItem("username"),
      api_key: localStorage.getItem("apiKey"),
      user: localStorage.getItem("userID")
    }, {
      'name': $scope.optionText,
      'votes': 0
    }, function() {
      $location.path('/list');
    });
  }
}
