var app = angular.module("oha",
        // Dependencies
        ['ui.bootstrap',
         'angularModalService',
         'angularUtils.directives.dirPagination',
         'ngSanitize',
         'oha.routes',
         'oha.listings',
       ]);


app.config(function($interpolateProvider) {
            $interpolateProvider.startSymbol('[{');
            $interpolateProvider.endSymbol('}]');
       });
