var app = angular.module("oha.listings", []);


app.controller("displaytable", function($scope, $http){

    $scope.headings = [];


    $scope.grants = [];

    $http.get('/loadtable').then(function(response) {
      response_data = response.data;
      $scope.headings = response_data.schema
                        .fields.map(function(item) { return item['name']; });
      $scope.grants = response_data.data;

    }, function(error) {

    });


    $scope.has_results = true;

});
