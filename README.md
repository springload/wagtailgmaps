wagtailgmaps
==================

Maps for Wagtail address fields

# Quickstart

``` $ pip install wagtailgmaps [GITHUB SSH URI]```

add wagtailgmaps to your settings.py in the INSTALLED_APPS section:

```
...
    'modelcluster',
    'wagtailgmaps',
    'core',
    'wagtail.contrib.wagtailsitemaps',
...
```

Add default settings:

```
...
WAGTAIL_ADDRESS_MAP_CENTER = 'Wellington, New Zealand'
WAGTAIL_ADDRESS_MAP_ZOOM = 8
...
```

Set class in your panel:

```
FieldPanel('address', classname="gmap")
```

Yuuhuuu!