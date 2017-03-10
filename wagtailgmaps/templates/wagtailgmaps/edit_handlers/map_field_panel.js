$(document).ready(function() {

    // Declare var params only first time
    try {
        if (!params) {
            var params = {};
        }
    } catch(e) {
        var params = {};
    }
    // Initialize the map after page loading. Pass all necessary params to identify everything related to this map
    params["{{ map_id }}"] = {"map_id": "{{ map_id }}", "zoom": {{ zoom }}};
    {% if address %}
        params["{{ map_id }}"]["address"] = "{{ address }}";
    {% endif %}
    document.addEventListener('wagtailmaps_ready', function (event) {
        // Wait until all the maps related functions are available and ready
        initialize_map(params["{{ map_id }}"]);
    });

});
