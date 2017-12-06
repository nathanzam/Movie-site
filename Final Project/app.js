(function() {
  'use strict';

  var app = angular.module('shawshank', ['store-products'])

    app.controller("StoreCtrl", function($http, $scope) {
      $http.get("./reviews.json").then(function (response) {
        $scope.products = response.data;

      });
    })

    app.controller('MovieCtrl', function($scope, $http) {

      $scope.today = d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate();

      $scope.queryZip = function(zip) {
        $http.get('http://data.tmsapi.com/v1.1/movies/showings?api_key=27ax2xgbtpbdkbv8337nf4p9&zip=' + $scope.userInput + '&startDate=' + today).then(function(response) {
          $scope.movies = response.data;
        });
      };
    });

    app.controller("ReviewCtrl");

}());
