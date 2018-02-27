from django.conf import settings
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.images import urls as wagtailimages_urls

try:
    from django.urls import include, url  # Use `path` once Django<2.0 support is dropped
except ImportError:
    from django.conf.urls import include, url


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
