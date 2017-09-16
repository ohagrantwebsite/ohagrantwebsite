var app = angular.module("oha.listings", []);


app.controller("displaytable", function($scope, $state, $http){

    $scope.headings = [];
    $scope.has_results = -1;
    $scope.grants = [];

    $scope.totalGrants = 0;
    $scope.grantsPerPage = 10;

    $scope.pagination = {
        current: 1
    };

    var filter = {
                    'column' : 0,
                    'operator' : 0,
                    'value' : 0
                  }

    getFilterDropdowns();

    getResultsPage(1);


    $scope.open_analyze = function() {
        $state.go('visualizer');
    }


    function getFilterDropdowns() {
        $http.get('/loadsearch').then(function(response) {
            response_data = response.data;



        }, function(error) {



        });


    }

    function getResultsPage(pageNumber) {
          var data = {
                  page: pageNumber,
                  per_page: 10,
                  filters: []
              }

          $http.post('/loadtable', data).then(function(response) {
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
