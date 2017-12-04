var map;
var geocoder;

function initMap() {
  var potomac = {
    lat: 39.0183,
    lng: -77.233
  };
  var myOptions = {
    zoom: 12,
    center: potomac
  };
  geocoder = new google.maps.Geocoder();
  map = new google.maps.Map(document.getElementById('map'), myOptions);
};

function codeAddress() {
  var sAddress = document.getElementById("zip").value;
  geocoder.geocode({
    'address': sAddress
  }, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      map.setCenter(results[0].geometry.location);
    }
  });
};
