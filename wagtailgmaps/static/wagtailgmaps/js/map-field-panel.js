class MapInputController extends window.StimulusModule.Controller {
    static targets = ["map", "textbox"];
    connect() {
        console.log(
            "MapInputController has connected:",
            this.element.innerText,
            this.mapTarget,
            this.textboxTarget,
            this.element.dataset
        );

        // One geocoder var to rule them all
        this.geocoder = new google.maps.Geocoder();

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

        console.log("MapInputController connecting complete");
        this.initialize_map({
            address: this.element.dataset.address,
            zoom: Number(this.element.dataset.zoom),
            latlngMode: Boolean(this.element.dataset.latlngMode),
        });
    }

    // Method to initialize a map and all of its related components (usually address input and marker)
    initialize_map(params) {
        console.log("Starting initialize_map");

        const controller = this;
        // Get latlong from address to initialize map
        this.geocoder.geocode(
            { address: params.address },
            function (results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                    controller.set_address(
                        results[0].geometry.location,
                        params.zoom,
                        params.latlngMode
                    );
                } else {
                    alert(
                        "Geocode was not successful for the following reason: " +
                            status
                    );
                }
            }
        );
        console.log("Finishing initialize_map");
    }

    // Get formatted address from LatLong position
    geocodePosition(pos, input, latlngMode) {
        this.geocoder.geocode(
            {
                latLng: pos,
            },
            function (responses) {
                if (responses && responses.length > 0) {
                    if (latlngMode) {
                        input.value =
                            String(responses[0].geometry.location.lat()) +
                            ", " +
                            String(responses[0].geometry.location.lng());
                    } else {
                        input.value = responses[0].formatted_address;
                    }
                } else {
                    alert("Cannot determine address at this location.");
                }
            }
        );
    }

    // Get LatLong position and formatted address from inaccurate address string
    geocodeAddress(address, input, latlngMode, marker, map) {
        this.geocoder.geocode({ address: address }, function (results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                marker.setPosition(results[0].geometry.location);
                if (latlngMode) {
                    input.value =
                        String(results[0].geometry.location.lat()) +
                        ", " +
                        String(results[0].geometry.location.lng());
                } else {
                    input.value = results[0].formatted_address;
                }
                map.setCenter(results[0].geometry.location);
            } else {
                alert(
                    "Geocode was not successful for the following reason: " +
                        status
                );
            }
        });
    }

    set_address(latlng, zoom, latlngMode) {
        // Create map options and map
        var mapOptions = {
            zoom: zoom,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
        };

        this.map = new google.maps.Map(this.mapTarget, mapOptions);
        this.marker = new google.maps.Marker({
            position: latlng,
            map: this.map,
            draggable: true,
        });

        const controller = this;
        // Set events listeners to update marker/input values/positions
        google.maps.event.addListener(this.marker, "dragend", function (event) {
            controller.geocodePosition(
                controller.marker.getPosition(),
                controller.textboxTarget,
                latlngMode
            );
        });
        google.maps.event.addListener(this.map, "click", function (event) {
            controller.marker.setPosition(event.latLng);
            controller.geocodePosition(
                controller.marker.getPosition(),
                controller.textboxTarget,
                latlngMode
            );
        });

        // Event listeners to update map when press enter or tab
        $(this.textboxTarget).bind("enterKey", function (event) {
            controller.geocodeAddress(
                this.value,
                controller,
                latlngMode,
                controller.marker,
                controller.map
            );
        });

        $(this.textboxTarget).keypress(function (event) {
            if (event.keyCode == 13) {
                event.preventDefault();
                $(this).trigger("enterKey");
            }
        });
    }
}

window.wagtail.app.register("map-input", MapInputController);
