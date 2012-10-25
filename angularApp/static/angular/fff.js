angular.module('fff', ['tastypieModule']).
  config(function($routeProvider) {
    $routeProvider.
      when('/', {controller:ListCtrl, templateUrl:'list.html'}).
      //when('/edit/:projectId', {controller:EditCtrl, templateUrl:'detail.html'}).
      when('/new', {controller:CreateCtrl, templateUrl:'add_option.html'}).
      otherwise({redirectTo:'/'});
  });
 
 
function ListCtrl($scope, $timeout, FoodOptions) {
    $scope.food_options = FoodOptions.get();
    setInterval(function(){
        $scope.food_options = FoodOptions.get();
    },5000);
}

function CreateCtrl($scope, $http, FoodOptions){
    $scope.addOption = function() {
        FoodOptions.update(function() {
            {name: $scope.optionText}
        });
        console.log({name: $scope.optionText});
        
        //$http.post('http://192.168.91.20/api/food/', {name: $scope.optionText}, withCredentials: true).success();
        
        
                /*
$.ajax({
  type: 'POST',
  url: 'http://192.168.91.20/api/food/',
  data: '{"name":"'+$scope.optionText+'"}',
  dataType: "application/json",
  contentType: "application/json",
  success: console.log('jquery worked')
}); */
        
    };
}