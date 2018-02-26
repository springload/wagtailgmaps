from __future__ import absolute_import, unicode_literals

import json
import random
import string

import wagtail
from django.conf import settings
from django.forms import TextInput
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.utils.widgets import WidgetWithScript


def random_string(length=6, chars=string.ascii_lowercase):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))


class MapInput(WidgetWithScript, TextInput):
    template_name = 'wagtailgmaps/forms/widgets/map_input.html'

    def __init__(self, default_centre, zoom, latlng, map_id, attrs=None):
        self.default_centre = default_centre
        self.zoom = zoom
        self.latlng = latlng
        self.map_id = map_id

        try:
            self.apikey = settings.WAGTAIL_ADDRESS_MAP_KEY
        except AttributeError:
            raise Exception('Google Maps API key is missing from settings')

        super().__init__(attrs)

    def get_map_centre(self, value):
        return value or self.default_centre

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        context.update({
            'address': self.get_map_centre(value),
            'zoom': self.zoom,
            'map_id': self.map_id,
            'latlng': self.latlng,
            'gmaps_api_key': self.apikey,
        })

        return context

    def build_attrs(self, base_attrs, extra_attrs=None):
        if extra_attrs is None:
            extra_attrs = {}

        extra_attrs.update({
            'data-latlng': self.latlng,
        })

        return super().build_attrs(base_attrs, extra_attrs)

    def render_js_init(self, id_, name, value):
        options = {
            'map_id': self.map_id,
            'address': self.get_map_centre(value),
            'zoom': self.zoom,
        }
        return (
            'document.addEventListener("wagtailmaps_ready", function(e){{'
            'window.initialize_map({opts});'
            '}});'
        ).format(opts=json.dumps(options))


class MapFieldPanel(FieldPanel):
    def __init__(self, field_name, *args, **kwargs):
        self.default_centre = kwargs.pop('centre', getattr(settings, 'WAGTAIL_ADDRESS_MAP_CENTER', None))
        self.zoom = kwargs.pop('zoom', getattr(settings, 'WAGTAIL_ADDRESS_MAP_ZOOM', 8))
        self.latlng = kwargs.pop('latlng', False)
        self.map_id = None  # Will be populated by `on_model_bound`

        super().__init__(field_name, *args, **kwargs)

    def clone(self):
        instance = super().clone()

        instance.default_centre = self.default_centre
        instance.zoom = self.zoom
        instance.latlng = self.latlng
        instance.map_id = self.map_id

        return instance

    def on_model_bound(self):
        super().on_model_bound()
        self.map_id = random_string()

    def classes(self):
        classes = super().classes()
        classes.append('wagtailgmap')
        return classes

    def widget_overrides(self):
        map_input = MapInput(
            default_centre=self.default_centre,
            zoom=self.zoom,
            latlng=self.latlng,
            map_id=self.map_id,
        )
        return {self.field_name: map_input}
