(function() {
  'use strict';

  var app = angular.module("store-products", [])

  app.directive("myHeader", function() {
    return {
      templateUrl: "./partials/header.html"
    }
  });

  app.directive("myFooter", function() {
    return {
      templateUrl: "./partials/footer.html"
    }
  })
}());
