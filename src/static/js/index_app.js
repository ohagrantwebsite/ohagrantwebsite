var app = angular.module("oha_index",
        // Dependencies
        ['ui.bootstrap',
         'satellizer',
         'angularModalService',
         'angularUtils.directives.dirPagination',
         'slickCarousel',
         'ngSanitize',
         'oha_index.components',
       ],
       function($interpolateProvider) {
            $interpolateProvider.startSymbol('[{');
            $interpolateProvider.endSymbol('}]');
  });
