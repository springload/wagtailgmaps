from django import template
from django.conf import settings
import uuid

register = template.Library()


@register.inclusion_tag('wagtailgmaps/test.html')
def test_tag(text, moretext):
    return {'var': text, 'var2': uuid.uuid4()}


# Map template
@register.inclusion_tag('wagtailgmaps/map_editor.html')
def map_editor(address, width, width_units, height, height_units, zoom):

    if address is None:
        address = settings.WAGTAIL_ADDRESS_MAP_CENTER

    map_id = uuid.uuid4()  # Something a bit simpler would be probably ok too..

    if zoom is None:
        zoom = settings.WAGTAIL_ADDRESS_MAP_ZOOM

    return {
        'map_id': map_id,
        'address': address,
        'zoom': zoom,
        'width': width,
        'width_units': width_units,
        'height': height,
        'height_units': height_units,
    }
