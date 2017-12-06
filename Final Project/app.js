(function() {
  'use strict';

  var app = angular.module('shawshank', ['store-products']);


  app.controller("StoreCtrl", function($http, $scope) {
    $http.get("./reviews.json").then(function(response) {
      $scope.products = response.data;
    });
  });

  app.controller('MovieCtrl', function($scope, $http) {

    var d = new Date();
    var today = d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate();

    $scope.today = d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate();

    $scope.queryZip = function(zip) {
      $http.get('http://data.tmsapi.com/v1.1/movies/showings?api_key=gyqhhfjsvbzvhqgm8rjjpvrk&zip=' + $scope.userInput + '&startDate=' + today).then(function(response) {
        $scope.movies = response.data;
      });
    };
  });

  app.controller("ReviewCtrl");

}());

var apikey = "gyqhhfjsvbzvhqgm8rjjpvrk";
// var apikey = "gkj8dsj2ha89jwfu3x59p2sh";
// var apikey = "vzxkgktf4t6jmkqnkv39c3zh";
