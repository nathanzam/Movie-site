var d = new Date();
var day = d.getDate();
var month = d.getMonth() + 1;
var year = d.getFullYear();
var today = (year + "-" + month + "-" + day);

$(".submit-city").on("click", function() {
  var inputValue = $("#zip").val();
  if(inputValue == '') {
    $("#zip").after("<div class='alert alert-danger'>Enter a valid zip code</div>");
  } else {
    $.get("http://data.tmsapi.com/v1.1/movies/showings?startDate=" + today + "&radius=20&zip=" + inputValue + "&api_key=gyqhhfjsvbzvhqgm8rjjpvrk", function (response){
      var data = response;
      $("#title").html(data.title);
      $("#directors").html("Director :"(data.directors));
      $("#top_cast").html("Starring " + (data.topCast));
      $("#ratings").html("Rating: " + (data.ratings.code));
      $("#short_description").html("Synopsis: " + (data.shortDescription));
      $("#theater_name").html("Theater :"(data.showtimes.theatre.name));
      $("#showtime").html("Showtime :"(data.showtimes.dateTime));
      $("#quals").html(data.showtimes.quals);
      $("#poster").html(data.preferredImage.uri);
    })
  }
});
