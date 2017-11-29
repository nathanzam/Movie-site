(function() {
  'use strict';

  var app = angular.module('shawshank', ['store-products'])

    app.controller("StoreCtrl", function($http, $scope) {
      $http.get("./reviews.json").then(function (response) {
        $scope.products = response.data;

      });
    })

    app.controller("ReviewCtrl");

}());
