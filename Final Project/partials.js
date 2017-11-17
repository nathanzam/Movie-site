(function() {
  'use strict';

  var app = angular.module("store-products", [])

  app.directive("myHeader", function() {
    return {
      templateUrl: "./partials/header.html",
      controller: function ($scope)
    }
  })
  
  app.directive("myFooter", function() {
    return {
      templateUrl: "./partials/footer.html",
      controller: function ($scope)
    }
  })
}());
