from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html_join

from wagtail.wagtailcore import hooks


@hooks.register('insert_editor_js')
def editor_js():
    """
    Add extra JS files to the admin
    """

    js_files = [
        static('wagtailgmaps/js/map-field.js'),
    ]
    js_includes = format_html_join(
        '\n', '<script src="{0}"></script>',
        ((filename,) for filename in js_files)
    )

    return js_includes


@hooks.register('insert_global_admin_css')
def admin_css():
    """
    Add extra CSS files to the admin
    """
    css_files = [
        static('wagtailgmaps/css/admin.css'),
    ]

    css_includes = format_html_join(
        '\n', '<link rel="stylesheet" href="{0}">',
        ((filename,) for filename in css_files)
    )

    return css_includes
