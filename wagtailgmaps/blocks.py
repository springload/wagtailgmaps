from wagtail import blocks
from django.conf import settings

from wagtailgmaps.widgets import MapInput


class MapBlock(blocks.CharBlock):
    class Meta:
        icon = "site"
        template = "wagtailgmaps/blocks/map_block.html"

    def __init__(
        self, *args, latlngMode=False, default_centre=None, zoom=None, **kwargs
    ):
        kwargs["form_classname"] = (
            kwargs.get("form_classname", "") + " gmap gmap--latlng"
        )
        super().__init__(*args, **kwargs)
        self.field.widget = MapInput(
            default_centre=default_centre or settings.WAGTAIL_ADDRESS_MAP_CENTER,
            zoom=zoom or settings.WAGTAIL_ADDRESS_MAP_ZOOM,
            latlngMode=latlngMode,  # 'latlngMode' will always store lat & lng instead of address
        )

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=None)
        context["api_key"] = getattr(settings, "GOOGLE_MAPS_KEY", "")
        return context
