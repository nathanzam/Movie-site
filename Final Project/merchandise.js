(function() {
  'use strict';

  angular
  .module("merch", ["store-products"])

    .controller("StoreCtrl", function($http, $scope) {
      $http.get("./merchandise.json").then(function (response) {
        $scope.products = response.data;
      });
    })
}());
