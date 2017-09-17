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

    getResultsPage(1);


    $scope.open_analyze = function() {
        $state.go('visualizer');
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


app.controller("searchctrl", function($scope, $state, $http){

    $scope.dropdown_button_name = 'Select Field';

    $scope.ctrl = {};
    $scope.ctrl.query = '';
    $scope.ctrl.msg = 'Search';
    $scope.ctrl.dataList = [];//getFilterDropdowns('Fiscal Year');

    $scope.dropdown_data = null;

    $scope.refresh_dropdown = function(field) {
      response_data = $scope.dropdown_data;
      if (response_data.hasOwnProperty(field)) {
        $scope.ctrl.dataList = response_data[field];
        $scope.ctrl.msg = field;
        $scope.dropdown_button_name = field;
      }
      else {
        $scope.ctrl.dataList = [];
        $scope.ctrl.msg = field;
        $scope.dropdown_button_name = field;
      }
    }






    $http.get('/loadsearch').then(function(response) {
        $scope.dropdown_data = response.data;
        $scope.refresh_dropdown('Project');
        $scope.ctrl.msg = 'Search';
    }, function(error) {

    });
});
