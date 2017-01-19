import string
import random
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.conf import settings
from wagtail.wagtailadmin.edit_handlers import (
    BaseCompositeEditHandler,
    FieldPanel,
    widget_with_script,
)


def random_string(length=6, chars=string.ascii_lowercase):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))


class BaseMapFieldPanel(BaseCompositeEditHandler):
    template = 'wagtailgmaps/edit_handlers/map_field_panel.html'
    js_template = 'wagtailgmaps/edit_handlers/map_field_panel.js'

    def classes(self):
        classes = super(BaseMapFieldPanel, self).classes()
        classes.append('multi-field')

        return classes

    def render(self):

        if (self.centre is None) or (self.centre == ''):
            try:
                self.centre = settings.WAGTAIL_ADDRESS_MAP_CENTER
            except AttributeError:
                pass

        try:
            selected_location = self.children[0].form[self.fieldname].value()
            if selected_location:
                self.centre = selected_location
        except KeyError:
            pass

        map_id = random_string()

        if self.zoom is None:
            try:
                self.zoom = settings.WAGTAIL_ADDRESS_MAP_ZOOM
            except AttributeError:
                self.zoom = 8

        try:
            apikey = settings.WAGTAIL_ADDRESS_MAP_KEY
        except AttributeError:
            raise Exception('Google Maps API key is missing from settings')

        width = 100
        width_units = '%'
        height = 300
        height_units = 'px'

        ctx = {
            'self': self,
            'map_id': map_id,
            'address': self.centre,
            'zoom': self.zoom,
            'width': width,
            'width_units': width_units,
            'height': height,
            'height_units': height_units,
            'gmaps_api_key': apikey,
            'latlng': self.latlng,
        }

        js = mark_safe(render_to_string(self.js_template, ctx))
        fieldset = render_to_string(self.template, ctx)
        return widget_with_script(fieldset, js)


class MapFieldPanel(object):
    def __init__(self, fieldname, heading='Location', classname='', latlng=False, centre='', zoom=8):
        self.children = [
            FieldPanel(fieldname),
        ]
        self.fieldname = fieldname
        self.heading = heading
        self.classname = classname
        self.centre = centre
        self.zoom = zoom
        self.latlng = latlng

    def bind_to_model(self, model):
        return type(str('_MapFieldPanel'), (BaseMapFieldPanel,), {
            'model': model,
            'children': [child.bind_to_model(model) for child in self.children],
            'fieldname': self.fieldname,
            'heading': self.heading,
            'classname': self.classname,
            'centre': self.centre,
            'zoom': self.zoom,
            'latlng': self.latlng,
        })
