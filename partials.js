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
  app.controller("reviewCtrl", function($http, $scope) {
    $http.get("./reviews.json").then(function (response) {
      $scope.reviews = response.data;
    });
  })
  app.directive("companyReviews", function () {
    return {
      templateUrl: "./partials/company-reviews.html",
      controller:  function($scope) {
        $scope.review = {};

        $scope.addReview = function (page) {
          page.reviews.push($scope.review);
          $scope.review = {};
        }
      }
    }
  })
  app.controller("merchCtrl", function($http, $scope) {
    $http.get("http://127.0.0.1:5000/").then(function (response) {
      $scope.products = response.data;
      });
    })
}());
