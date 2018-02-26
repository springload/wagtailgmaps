from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel
from wagtail.core.models import Page

from wagtailgmaps.edit_handlers import MapFieldPanel



class MapPage(Page):
    formatted_address = models.CharField(max_length=255)
    latlng_address = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        MapFieldPanel('formatted_address'),
        MultiFieldPanel([
            MapFieldPanel('latlng_address', latlng=True),
        ], 'LatLng Address (nested)')
    ]
