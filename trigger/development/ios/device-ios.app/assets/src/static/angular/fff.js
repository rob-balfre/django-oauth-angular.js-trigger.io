angular.module('fff', ['tastypieModule']).
  config(function($routeProvider) {
    $routeProvider.
      when('/', {controller:HomeCrtl, templateUrl:'home.html'}).
      when('/list', {controller:ListCtrl, templateUrl:'list.html'}).
      when('/new', {controller:CreateCtrl, templateUrl:'add_option.html'}).
      otherwise({redirectTo:'/'});
  });

function HomeCrtl($scope, $location) {
   $scope.userLogin = function() {
       forge.tabs.openWithOptions({
           url: 'http://192.168.91.20/accounts/twitter/login/',
           pattern: 'http://192.168.91.20/auth/*'
        }, function (data) {
            forge.logging.log(data.url);
            $scope.$apply(function() {
                $location.path('/list');
            });
        });
    }; 
};

function ListCtrl($scope, $http, FoodOptions) {
   $scope.food_options = FoodOptions.get();   
};

function CreateCtrl($scope, $http, FoodOptions){
    $scope.addOption = function() {
        //$http.post('http://192.168.91.20/api/food/', {name: $scope.optionText}, {withCredentials: false});

        $.ajax({
            type: 'POST',
            url: 'http://192.168.91.20/api/food/?username=testy&api_key=32331180f4d70523597be5a027223a9cfaf90fdd',
            data: '{"name":"'+$scope.optionText+'"}',
            contentType: "application/json"
            //dataType: 'json',
            //processData: false
        }).done(function(data) { console.log('sent: '+data) });
    };
}