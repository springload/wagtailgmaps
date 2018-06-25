$(document).ready(function() {

  // One geocoder var to rule them all
  var geocoder = new google.maps.Geocoder();

  // Get formatted address from LatLong position
  function geocodePosition(pos, input, latlngMode) {
    geocoder.geocode({
      latLng: pos
    }, function(responses) {
      if (responses && responses.length > 0) {
          $input = $(input);
          if (latlngMode) {
            $input.val(
              String(responses[0].geometry.location.lat()) + ', ' + String(responses[0].geometry.location.lng())
            );
          } else {
            $input.val(responses[0].formatted_address);
          }
      } else {
        alert('Cannot determine address at this location.');
      }
    });
  }

  // Get LatLong position and formatted address from inaccurate address string
  function geocodeAddress(address, input, latlngMode, marker, map) {
    geocoder.geocode({'address': address}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        marker.setPosition(results[0].geometry.location);
        $input = $(input);
        if (latlngMode) {
          $input.val(
            String(results[0].geometry.location.lat()) + ', ' + String(results[0].geometry.location.lng())
          );
        } else {
          $input.val(results[0].formatted_address);
        }
        map.setCenter(results[0].geometry.location);
      } else {
        alert("Geocode was not successful for the following reason: " + status);
      }
    });
  }

  function set_address(mapElem, latlng, mapId, map_key, zoom, latlngMode, map, marker){
        mapElem[map_key] = document.getElementById(mapId);
        // Usually the address input is the first input sibling of the map container..
        mapElem.input = $("#" + mapId).parent().find("input:first");
        // Create map options and map
        var mapOptions = {
            zoom: zoom,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        map[map_key] = new google.maps.Map(mapElem[map_key], mapOptions);
        marker[map_key] = new google.maps.Marker({
          position: latlng,
          map: map[map_key],
          draggable: true
        });
        // Set events listeners to update marker/input values/positions
        google.maps.event.addListener(marker[map_key], 'dragend', function(event) {
          geocodePosition(marker[map_key].getPosition(), mapElem.input, latlngMode);
        });
        google.maps.event.addListener(map[map_key], 'click', function(event) {
          marker[map_key].setPosition(event.latLng);
          geocodePosition(marker[map_key].getPosition(), mapElem.input, latlngMode);
        });

        // Event listeners to update map when press enter or tab
        $(mapElem.input).bind("enterKey",function(event) {
          geocodeAddress($(this).val(), this, latlngMode, marker[map_key], map[map_key]);
        });

        $(mapElem.input).keypress(function(event) {
            if(event.keyCode == 13)
            {
              event.preventDefault();
              $(this).trigger("enterKey");
            }
        });
      }

  // Method to initialize a map and all of its related components (usually address input and marker)
  window.initialize_map = function (params) {

      // Get latlong form address to initialize map
      geocoder.geocode( { "address": params.address}, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
          set_address({}, results[0].geometry.location, params.map_id, params.map_id, params.zoom, params.latlng, {}, {});
        } else {
          alert("Geocode was not successful for the following reason: " + status);
        }
      });

  };

  // Trigger the event so the maps can start doing their things
  var event; // The custom event that will be created

  if (document.createEvent) {
    event = document.createEvent("HTMLEvents");
    event.initEvent("wagtailmaps_ready", true, true);
  } else {
    event = document.createEventObject();
    event.eventType = "wagtailmaps_ready";
  }

  event.eventName = "wagtailmaps_ready";

  if (document.createEvent) {
    document.dispatchEvent(event);
  } else {
    document.fireEvent("on" + event.eventType, event);
  }

});
