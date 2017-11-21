(function() {
  'use strict';

  var app = angular.module('shawshank', ['store-products'])

    app.controller("StoreCtrl", function($http, $scope) {
      $http.get("").then(function (response) {
        $scope.products = response.data;

      });
    })

    app.controller("ReviewCtrl");

}());
