from django.conf import settings
from django.forms import Media, TextInput


class MapInput(TextInput):
    template_name = "wagtailgmaps/forms/widgets/map_input.html"

    def __init__(self, default_centre, zoom, latlngMode, attrs=None):
        self.default_centre = default_centre
        self.zoom = zoom
        self.latlngMode = latlngMode
        attrs = (attrs or {}) | {"data-map-input-target": "textbox"}

        try:
            self.apikey = settings.WAGTAIL_ADDRESS_MAP_KEY
        except AttributeError:
            raise Exception("Google Maps API key is missing from settings")

        super().__init__(attrs)

    def get_map_centre(self, value):
        return value or self.default_centre

    def get_map_id(self, field_id):
        assert field_id
        return "{}-map-canvas".format(field_id)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        context.update(
            {
                "address": self.get_map_centre(value),
                "gmaps_api_key": self.apikey,
                "latlngMode": self.latlngMode,
                "map_id": self.get_map_id(attrs["id"]),
                "zoom": self.zoom,
                "default_centre": self.default_centre,
            }
        )

        return context

    @property
    def media(self):
        maps_api_js = "https://maps.googleapis.com/maps/api/js?key={}".format(
            settings.WAGTAIL_ADDRESS_MAP_KEY
        )
        language = getattr(settings, "WAGTAIL_ADDRESS_MAP_LANGUAGE", None)
        if language:
            maps_api_js += "&language={}".format(language)

        return Media(
            css={"screen": ("wagtailgmaps/css/admin.css",)},
            js=(maps_api_js, "wagtailgmaps/js/map-field-panel.js"),
        )
