var map;
var geocoder;
var infoWindow;
var latitude = '';
var longitude = '';

function convertZip() {
  var address = $('#zip').val();
  geocoder.geocode( { 'address': address}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
       latitude = results[0].geometry.location.lat();
       longitude = results[0].geometry.location.lng();
    } else {
      console.log(status)
    }
  });
}

function initMap() {
  var potomac = {
    lat: 39.0183,
    lng: -77.233
  };
  var myOptions = {
    zoom: 12,
    center: potomac
  };
  map = new google.maps.Map(document.getElementById('map'), myOptions);

  var request = {
    location: potomac,
    radius: 15000,
    type: ["movie_theater"]
  };

  infoWindow = new google.maps.InfoWindow();

  var service = new google.maps.places.PlacesService(map);

  service.nearbySearch(request, callback);

  geocoder = new google.maps.Geocoder();
  service = new google.maps.places.PlacesService(map);

};

function performSearch() {
  var request = {
    bounds: map.getBounds(),
    keyword: 'best view'
  };
  service.radarSearch(request, callback);
}

function callback(results, status) {
  if (status !== google.maps.places.PlacesServiceStatus.OK) {
    console.error(status);
    return;
  }
  for (var i = 0, result; result = results[i]; i++) {
    addMarker(result);
  }
}

function codeAddress() {
  var sAddress = document.getElementById("zip").value;
  geocoder.geocode({
    'address': sAddress
  }, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      map.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
        map: map,
        position: results[0].geometry.location
      });
      var request = {
        location: results[0].geometry.location,
        radius: 8048,
        type: ['movie_theater']
      };
      infowindow = new google.maps.InfoWindow();
      var service = new google.maps.places.PlacesService(map);
      service.nearbySearch(request, callback);
      google.maps.event.addListener(marker, 'click', function() {
        infoWindow.setContent(place.name);
        infoWindow.open(map, this);
      })
    }
  });
};

function addMarker(place) {
  var placeLoc = place.geometry.location;
  var marker = new google.maps.Marker({
    map: map,
    position: place.geometry.location
  });

  google.maps.event.addListener(marker, 'click', function() {
    infoWindow.setContent(place.name);
    infoWindow.open(map, this);
  })
}
  //
  // var markers = []
  //
  // for(i = 0; i < markers.length; i++) {
  //   addMarkers(markers[i]);
  // }
  //
  // function addMarkers(coordinates) {
  //   var marker = new google.maps.Marker({
  //     position = coordinates,
  //     map = map
  //   })
  // }
  // function markerLocations(){
  //
  // }
  // "api.citygridmedia.com/content/places/v2/search/where?type=movietheater&where=" + zipCode + "&publisher=test&format=json"
