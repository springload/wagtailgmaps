from django.db import models
from wagtail.admin.panels import MultiFieldPanel
from wagtail.models import Page

from wagtailgmaps.panels import MapFieldPanel


class MapPage(Page):
    formatted_address = models.CharField(max_length=255)
    latlng_address = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        MapFieldPanel("formatted_address"),
        MultiFieldPanel(
            [
                MapFieldPanel("latlng_address", latlngMode=True),
            ],
            "LatLng Address (nested)",
        ),
    ]
