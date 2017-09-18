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

    $scope.current_filters = [];

    $scope.indices = [];


    $scope.open_analyze = function() {
        $state.go('visualizer');
    }


    $scope.getResultsPage = function getResultsPage(pageNumber, filters) {
          var data = {
                  page: pageNumber,
                  per_page: 10,
                  filters: filters
              }
          $scope.current_filters = filters;
          $http.post('/loadtable', data).then(function(response) {

                  function arraysEqual(arr1, arr2) {
                      if(arr1.length !== arr2.length)
                        return false;
                      for(var i = arr1.length; i--;) {
                        if(arr1[i] !== arr2[i])
                            return false;
                      }
                      return true;
                      }

                  response_data = response.data;
                  $scope.headings = response_data.schema
                                    .fields.map(function(item) {
                                                return item['name'];
                                                });
                  $scope.grants = response_data.data;

                  $scope.totalGrants = response_data.Elements;


                  if (!arraysEqual($scope.indices, response_data.indices)) {
                      $scope.indices = response_data.indices;
                      $scope.$broadcast('UPDATE_THE_CHART');
                  }
                  $scope.has_results = 1;




                  return true;
                }, function(error) {
                  return false;
                });
    }

    $scope.getResultsPage(1, []);

    $scope.pageChanged = function(newPage) {
      filters = $scope.current_filters;
      $scope.getResultsPage(newPage, filters);
    };

    $scope.get_indices = function() {
      return $scope.indices;
    }


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



    $scope.search = function(query, column) {

      operator = 'like';

      if (column == 'Grant Status ID') {
        column = 'GrantStatusId';
      }

      if (column == 'Fiscal Year' || column == 'Amount' || column == 'TOTAL # SERVED' || column == '# NH SERVED'  || column == 'GrantStatusId') {
        operator = 'equals';

      }

      var filter = [{
        'column' : column,
        'operator' : operator,
        'value' : query
      }];

      $scope.$parent.getResultsPage(1, filter);

    }


    $http.get('/loadsearch').then(function(response) {
        $scope.dropdown_data = response.data;
        $scope.refresh_dropdown('Project');
        $scope.dropdown_button_name = 'Select Field';
        $scope.ctrl.msg = 'Select Field';
    }, function(error) {

    });
});

app.controller("chartctrl", function($scope, $state, $http){

    $scope.chartimage = '';
    $scope.active_axis_name = 'Fiscal Year';

    $scope.refresh_chart = function(axis) {

        submit_axis = axis;
        if (submit_axis == 'Grant Status ID') {
          submit_axis = 'GrantStatusId';
        }
        data = {
          'indices' : $scope.$parent.get_indices(),
          'axis' : submit_axis,
        }
        $scope.active_axis_name = axis;

        $http.post('/loadchart', data, {responseType: "arraybuffer"}).then(function(response) {
            rawResponse = response.data;
            data64 = btoa(new Uint8Array(rawResponse)
                          .reduce((data, byte) => data + String.fromCharCode(byte), ''));
            newlink = 'data:image/gif;base64,' + data64;
            $scope.chartimage = newlink;
        }, function(error) {

        });
    }


     $scope.$on('UPDATE_THE_CHART', function() {
      $scope.refresh_chart($scope.active_axis_name);
    });


    $scope.refresh_chart('Fiscal Year');
});
