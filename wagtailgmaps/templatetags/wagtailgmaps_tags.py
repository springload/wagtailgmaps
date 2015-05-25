import uuid

from django import template
from django.conf import settings

from distutils.version import StrictVersion

from wagtailgmaps.utils import get_wagtail_version

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
def wagtail_version():
    """
    Return css folder used in the path of admin assets depending on the Wagtail version
    """
    current_version = get_wagtail_version()

    if StrictVersion(current_version) >= StrictVersion('1.0b2'):
        return 'css'
    else:
        return 'scss'
