var app = angular.module("oha",
        // Dependencies
        ['ui.bootstrap',
         'satellizer',
         'angularModalService',
         'angularUtils.directives.dirPagination',
         'slickCarousel',
         'ngSanitize',
         'oha.routes',
         'oha.index'

       ],
       function($interpolateProvider) {
            console.log("TEST");
            $interpolateProvider.startSymbol('[{');
            $interpolateProvider.endSymbol('}]');
  });
