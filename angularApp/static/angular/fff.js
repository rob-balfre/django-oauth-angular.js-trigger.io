angular.module('fff', ['tastypieModule']).
  config(function($routeProvider) {
    $routeProvider.
      when('/', {controller:ListCtrl, templateUrl:'list.html'}).
      //when('/edit/:projectId', {controller:EditCtrl, templateUrl:'detail.html'}).
      //when('/new', {controller:CreateCtrl, templateUrl:'detail.html'}).
      otherwise({redirectTo:'/'});
  });
 
 
function ListCtrl($scope, $timeout, FoodOptions) {
    $scope.food_options = FoodOptions.get();
    setInterval(function(){
        $scope.food_options = FoodOptions.get();
    },5000);
}