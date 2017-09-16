
var app = angular.module("oha.routes", ['ui.router', 'ngAnimate']);

/*
* Configurations for states for ui-router.
*
*/

app.config(function($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('');

    $stateProvider
    .state('list', {
      url: '',
      views: {
        '' : {
          templateUrl: 'static/components/listings/listings_wrapper.html',
        },
        'table@list' : {
          templateUrl: 'static/components/listings/listings_table.html',
        },
      },
      })

    .state('visualizer', {
      url: 'vis',
      views: {
        '' : {
          templateUrl: 'static/components/visualizer/visualizer_wrapper.html',
        },
        'plot@visualizer' : {
          templateUrl: 'static/components/listings/visualizer_plot.html',
        },
      },
      })

    });
