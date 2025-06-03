class MapInputController extends window.StimulusModule.Controller {
    static targets = ["map", "textbox"];
    connect() {
        // One geocoder var to rule them all
        this.geocoder = new google.maps.Geocoder();
        this.latlngMode = Boolean(this.element.dataset.latlngmode);
        this.zoom = Number(this.element.dataset.zoom);
        this.defaultCentre = this.element.dataset.defaultcentre;

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

        this.initialiseMap(this.textboxTarget.value);
    }

    // Get formatted address from LatLong position
    geocodePosition(pos, input) {
        const controller = this;
        this.geocoder.geocode(
            {
                latLng: pos,
            },
            function (responses) {
                if (responses && responses.length > 0) {
                    if (controller.latlngMode) {
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
    geocodeAddress(address, input, marker, map) {
        const controller = this;
        this.geocoder.geocode({ address: address }, function (results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                marker.setPosition(results[0].geometry.location);
                if (controller.latlngMode) {
                    input.value =
                        String(results[0].geometry.location.lat()) +
                        ", " +
                        String(results[0].geometry.location.lng());
                } else {
                    input.value = results[0].formatted_address;
                }
                map.setCenter(results[0].geometry.location);
            } else {
                alert("Address could not be found: " + status);
            }
        });
    }

    initialiseMap(initValue) {
        // Create map options and map
        const controller = this;
        const mapOptions = {
            zoom: this.zoom,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
        };

        controller.map = new google.maps.Map(controller.mapTarget, mapOptions);
        controller.marker = new google.maps.Marker({
            position: mapOptions.position,
            map: this.map,
            draggable: true,
        });

        // Set events listeners to update marker/input values/positions
        google.maps.event.addListener(
            controller.marker,
            "dragend",
            function (event) {
                controller.geocodePosition(
                    controller.marker.getPosition(),
                    controller.textboxTarget
                );
            }
        );
        google.maps.event.addListener(
            controller.map,
            "click",
            function (event) {
                controller.marker.setPosition(event.latLng);
                controller.geocodePosition(
                    controller.marker.getPosition(),
                    controller.textboxTarget
                );
            }
        );

        // Event listeners to update map when press enter or tab
        $(controller.textboxTarget).bind("enterKey", function (event) {
            controller.geocodeAddress(
                this.value,
                controller.textboxTarget,
                controller.marker,
                controller.map
            );
        });

        $(controller.textboxTarget).keypress(function (event) {
            if (event.keyCode == 13) {
                event.preventDefault();
                $(this).trigger("enterKey");
            }
        });

        // Set the map to the initial location
        controller.geocodeAddress(
            initValue || controller.defaultCentre,
            controller.textboxTarget,
            controller.marker,
            controller.map
        );
    }
}

window.wagtail.app.register("map-input", MapInputController);
