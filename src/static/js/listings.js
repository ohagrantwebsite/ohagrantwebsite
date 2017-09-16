var app = angular.module("oha.listings", []);


app.controller("displaytable", function($scope, $http){

    $scope.headings = [];
    $scope.has_results = -1;
    $scope.grants = [];

    $scope.totalGrants = 0;
    $scope.grantsPerPage = 10;

    $scope.pagination = {
        current: 1
    };

    var config = {
        params: {
            page: 1,
            per_page: 10,
          }
    }
    getResultsPage(1);


    function getResultsPage(pageNumber) {
          $http.get('/loadtable', config).then(function(response) {
            response_data = response.data;
            $scope.headings = response_data.schema
                              .fields.map(function(item) {
                                          return item['name'];
                                          });
            $scope.grants = response_data.data;

            $scope.totalGrants = response_data.Elements;

            $scope.has_results = 1;
          }, function(error) {

          });
    }

    $scope.pageChanged = function(newPage) {
      getResultsPage(newPage);
    };


});
