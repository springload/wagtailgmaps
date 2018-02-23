from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url

try:
    from wagtail.admin import urls as wagtailadmin_urls
    from wagtail.core import urls as wagtail_urls
    from wagtail.documents import urls as wagtaildocs_urls
    from wagtail.images import urls as wagtailimages_urls
except ImportError:
    from wagtail.wagtailadmin import urls as wagtailadmin_urls
    from wagtail.wagtailcore import urls as wagtail_urls
    from wagtail.wagtaildocs import urls as wagtaildocs_urls
    from wagtail.wagtailimages import urls as wagtailimages_urls

urlpatterns = [
    url(r'^admin/', include(wagtailadmin_urls)),

    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^images/', include(wagtailimages_urls)),

    url(r'', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
