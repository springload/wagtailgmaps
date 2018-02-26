from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.urls import include, path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.images import urls as wagtailimages_urls


urlpatterns = [
    path('admin/', include(wagtailadmin_urls)),

    path('documents/', include(wagtaildocs_urls)),
    path('images/', include(wagtailimages_urls)),

    path('', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
