from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html_join
from wagtail.wagtailcore import hooks


@hooks.register('insert_editor_js')
def editor_js():
    maps_js = 'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.WAGTAIL_ADDRESS_MAP_KEY)
    language = getattr(settings, 'WAGTAIL_ADDRESS_MAP_LANGUAGE')
    if language:
        maps_js += '&language={}'.format(language)
    js_files = (
        maps_js,
        static('wagtailgmaps/js/map-field-panel.js'),
    )
    js_includes = format_html_join(
        '\n',
        '<script type="text/javascript" src="{}"></script>',
        ((filename,) for filename in js_files)
    )
    return js_includes


@hooks.register('insert_editor_css')
def editor_css():
    css_files = (
        'wagtailgmaps/css/admin.css',
    )
    css_includes = format_html_join(
        '\n',
        '<link rel="stylesheet" href="{0}">',
        ((static(filename),) for filename in css_files)
    )
    return css_includes
