// var apikey = "gyqhhfjsvbzvhqgm8rjjpvrk";
var apikey = "gkj8dsj2ha89jwfu3x59p2sh";
var posters = [];
// var apikey = "vzxkgktf4t6jmkqnkv39c3zh";
var baseUrl = "http://data.tmsapi.com/v1.1";
var showtimesUrl = baseUrl + '/movies/showings';
var d = new Date();
var today = d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate();
$(".submit-zip").on("click", function() {
  var zipCode = $("#zip").val();
  // send off the query
  $.ajax({
   url: showtimesUrl,
       data: { startDate: today,
  zip: zipCode,
  jsonp: "dataHandler",
  api_key: apikey
 },
   dataType: "jsonp",
  });
});

// callback to handle the results
function dataHandler(data) {
  var zipCode = $("#zip").val();
 $(document.body).append('<p>Found ' + data.length + ' movies showing within 5 miles of ' + zipCode+':</p>');
 var movie_titles = []
 var movies = data.hits;
 var re =  / /gi;
 // console.log(posters);
 $.each(data, function(index, movie) {
   var movieData = '<div class="tile"><br/>';
   movieData += movie.title;
   movie_titles.push(movie.title);
   if (movie.ratings) { movieData += ' (' + movie.ratings[0].code + ') </div>' };
   $(document.body).append(movieData);
 });
 for(i=0; i<movie_titles.length; i++){
   var posterSite = "http://www.omdbapi.com/?t=justice+league&type=movie&apikey=58141393";
   // var posterSite = "http://www.omdbapi.com/?t=" + movie_titles[i].replace(re, "+").replace("+3D", "") + "&type=movie&apikey=58141393";
   $.ajax({
     url: posterSite,
     jsonp: "dataHandler",
     success: function(data)
     {
       posters.push(data);
     }
   })
 }
   console.log(movie_titles);
 }
 console.log(posters[0]['Poster']);
