// var apikey = "gyqhhfjsvbzvhqgm8rjjpvrk";
var apikey = "gkj8dsj2ha89jwfu3x59p2sh";
// var apikey = "vzxkgktf4t6jmkqnkv39c3zh";
var posters = [];
var baseUrl = "http://data.tmsapi.com/v1.1";
var d = new Date();
var today = d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate();
var zipCode = $('#zip').val();
var showtimesUrl = baseUrl + '/movies/showings&startDate=' + today + '&zip=' + zipCode + '&apikey=' + apikey;
  // window.onload = movieApiCall(20854);

function movieAPICall(zipCode) {
  $.ajax({
             url: showtimesUrl,
             type: 'GET',
             dataType: 'json'
         })
         .done(function(result) {
             //  console.log(result);
             displayQuery(result);
         })
 }

 function displayQuery(data) {
     console.log(data);
     var sendToPage = "";
     sendToPage += "<h1 class = zipcode> Movies showing within 5 miles of " + zipCode + "</h1>";
     $.each(data, function(index, movie) {
         sendToPage += "<div class='movie'>";
         sendToPage += "<button class='accordion'>";
         sendToPage += "<div class='panel'>";
         sendToPage += "<div class='movieTitle'>";
         sendToPage += "<a id=\"" + movie.title + "\" class='anchor'>.</a>";
         sendToPage += "<h1 class=\"" + movie.title + "\"><a href='" + movie.officialUrl + "' target='_blank'>" + movie.title + "</a></h1>";
         $.each(movie.ratings, function(ratingInxed, ratingValue) {
             sendToPage += "<p>" + ratingValue.code + '</p>';
         });
         sendToPage += "<p>" + movie.shortDescription + "<p>";
         sendToPage += "</button>";
         sendToPage += "</div>";
         $.each(movie.showtimes, function(showtimeIndex, showtimeValue) {
             sendToPage += "<div class='theater'>";
             sendToPage += "<div>" + showtimeValue.theatre.name + "</div>";
             sendToPage += "<div class='panel'>";
             sendToPage += "<p>" + showtimeValue.dateTime + "</p>";
             sendToPage += "</div>";
             sendToPage += "</div>";

         });
         sendToPage += "</div>";
         sendToPage += "</div>";
     });
     $('.theater-info ul').html(sendToPage);
 }

// $(document).ready(function() {
//     zipCode = $('#zip').val();
//
//     $('.zip-code').submit(function(event) {
//         event.preventDefault;
//         zipCode = $('#zip').val();
//         console.log("zipCode = ", zipCode);
//         movieApiCall(zipCode);
//     });
// });

 // for(i=0; i<movie_titles.length; i++){
 //   var posterSite = "http://www.omdbapi.com/?t=justice+league&type=movie&apikey=58141393";
 //   // var posterSite = "http://www.omdbapi.com/?t=" + movie_titles[i].replace(re, "+").replace("+3D", "") + "&type=movie&apikey=58141393";
 //   $.ajax({
 //     url: posterSite,
 //     jsonp: "dataHandler",
 //     success: function(data)
 //     {
 //       posters.push(data);
 //     }
 //   })
 // }
   // console.log(movie_titles);
 // console.log(posters[0]['Poster']);
