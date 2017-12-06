var apikey = "vzxkgktf4t6jmkqnkv39c3zh";
var baseUrl = "http://data.tmsapi.com/v1.1";
var showtimesUrl = baseUrl + '/movies/showings';
var d = new Date();
var today = d.getFullYear() + '-' + (d.getMonth()+1) + '-' + d.getDate();
$(".submit-zip").on("click", function() {
  var zipCode = $('#zip').val();

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

// callback to handle the results

function dataHandler(data) {
 $(document.body).append('<p>Found ' + data.length + ' movies showing within 5 miles of ' + zipCode+':</p>');
 var movies = data.hits;
$.each(data, function(index, movie) {
   var movieData = '<div class="tile"><img src="http://via.placeholder.com/150x350"><br/>';
   movieData += movie.title;
   if (movie.ratings) { movieData += ' (' + movie.ratings[0].code + ') </div>' };
   $(document.body).append(movieData);
 });
}
});
