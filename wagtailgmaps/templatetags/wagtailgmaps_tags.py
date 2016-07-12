import uuid

from django import template
from django.conf import settings

register = template.Library()


# Map template
@register.inclusion_tag('wagtailgmaps/map_editor.html')
def map_editor(address, width, width_units, height, height_units, zoom):
    """
    Tag to output a Google Map with the given attributes
    """
    if (address is None) or (address == ""):
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


@register.simple_tag
def google_maps_script():
    return '<script src="https://maps.googleapis.com/maps/api/js?key={}"></script>'.format(settings.WAGTAIL_ADDRESS_MAP_KEY)
