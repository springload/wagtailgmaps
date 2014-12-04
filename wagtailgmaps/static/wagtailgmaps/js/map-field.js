jQuery(document).ready(function() {
  
  google.maps.event.addDomListener(window, 'load', function() {
  
    // One geocoder var to rule them all
    var geocoder = new google.maps.Geocoder();

    // Get formatted address from LatLong position
    function geocodePosition(pos, input) {
      geocoder.geocode({
        latLng: pos
      }, function(responses) {
        if (responses && responses.length > 0) {
            $(input).val(responses[0].formatted_address);
        } else {
          alert('Cannot determine address at this location.');
        }
      });
    }

    // Get LatLong position and formatted address from inaccurate address string
    function geocodeAddress(address, input, marker, map) {
      geocoder.geocode( { 'address': address}, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
          marker.setPosition(results[0].geometry.location);
          $(input).val(results[0].formatted_address);
          map.setCenter(results[0].geometry.location);
        } else {
          alert("Geocode was not successful for the following reason: " + status);
        }
      });
    }

    function set_address(mapElem, latlng, mapId, map_key, zoom, map, marker){
          mapElem[map_key] = document.getElementById(mapId);
          // Usually the address input is the first input sibling of the map container..
          mapElem["input"] = $("#" + mapId).parent().find("input:first");
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
            geocodePosition(marker[map_key].getPosition(), mapElem["input"]);
          });
          google.maps.event.addListener(map[map_key], 'click', function(event) {
            marker[map_key].setPosition(event.latLng);
            geocodePosition(marker[map_key].getPosition(), mapElem["input"]);
          });
          
          // Event listeners to update map when press enter or tab
          $(mapElem["input"]).bind("enterKey focusout",function(event) {
            geocodeAddress($(this).val(), this, marker[map_key], map[map_key]);
          });

          $(mapElem["input"]).keypress(function(event) {
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
        geocoder.geocode( { 'address': params["address"]}, function(results, status) {
          if (status == google.maps.GeocoderStatus.OK) {
            //var latlng = results[0].geometry.location;
            set_address({}, results[0].geometry.location, "map-canvas-" + params["map_id"], params["map_id"], params["zoom"], {}, {});
          } else {
            alert("Geocode was not successful for the following reason: " + status);
          }
        });

    }

    // Trigger the event so the maps can start doing its things
    $.event.trigger({
      type:    "wagtailmaps_ready",
      message: "WagtailMaps are ready to be used!",
      time:    new Date()
    });

  });

}); 
