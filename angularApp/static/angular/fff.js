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

function CreateCtrl($scope, FoodOptions){
    $scope.addOption = function() {
        console.log($scope.optionText);
        FoodOptions.update(function() {
            ({'name': $scope.optionText});
        });
        console.log({name: $scope.optionText});
    };
}