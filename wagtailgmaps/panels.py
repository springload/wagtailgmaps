from django.conf import settings
from wagtail.admin.panels import FieldPanel

from .widgets import MapInput


class MapFieldPanel(FieldPanel):
    def __init__(self, field_name, *args, **kwargs):
        self.default_centre = kwargs.pop(
            "centre", getattr(settings, "WAGTAIL_ADDRESS_MAP_CENTER", None)
        )
        self.zoom = kwargs.pop("zoom", getattr(settings, "WAGTAIL_ADDRESS_MAP_ZOOM", 8))
        self.latlngMode = kwargs.pop("latlngMode", False)

        kwargs["widget"] = kwargs.get(
            "widget",
            MapInput(
                default_centre=self.default_centre,
                zoom=self.zoom,
                latlngMode=self.latlngMode,
            ),
        )

        super().__init__(field_name, *args, **kwargs)

    def clone(self):
        instance = super().clone()

        instance.default_centre = self.default_centre
        instance.zoom = self.zoom
        instance.latlngMode = self.latlngMode

        return instance

    def classes(self):
        classes = super().classes()
        classes.append("wagtailgmap")
        return classes
