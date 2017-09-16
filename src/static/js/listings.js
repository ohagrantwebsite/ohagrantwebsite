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

    getResultsPage(1);

    function getResultsPage(pageNumber) {
          var config = {
              params: {
                  page: pageNumber,
                  per_page: 10,
                  filters: [
                            {
                              column: 'None1',
                              operator: 'None',
                              value: 'None'
                            },
                            {
                              column: 'None2',
                              operator: 'None',
                              value: 'None'
                            }
                            ]
                }
              }

          $http.post('/loadtable', config).then(function(response) {
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
