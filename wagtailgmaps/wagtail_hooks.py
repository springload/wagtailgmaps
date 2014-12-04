from wagtail.wagtailcore import hooks
from django.conf import settings
from django.utils.html import format_html_join


@hooks.register('insert_editor_js')
def editor_js():
    """
    Add extra JS files to the admin
    """
    js_files = [
        'wagtailgmaps/js/map-field.js',
    ]
    js_includes = format_html_join(
        '\n',
        '<script type="text/javascript" src="{0}{1}"></script>',
        ((settings.STATIC_URL, filename) for filename in js_files)
    )

    return js_includes
