wagtailgmaps
==================

![Wagtailgmaps screenshot](http://i.imgur.com/9m9Gfcf.png)

Simple Google Maps address formatter for Wagtail fields.

# Quickstart

``` $ pip install git+git://github.com:springload/wagtailgmaps@0.1#egg=wagtailgmaps```

add wagtailgmaps to your `settings.py` in the INSTALLED_APPS section:

```
...
    'modelcluster',
    'wagtailgmaps',
    'wagtail.contrib.wagtailsitemaps',
...
```

Add a couple of necessary constants in your `settings.py` file:

```
...
WAGTAIL_ADDRESS_MAP_CENTER = 'Wellington, New Zealand'
WAGTAIL_ADDRESS_MAP_ZOOM = 8
...
```
`WAGTAIL_ADDRESS_MAP_CENTER` must be a properly formatted address. Also, remember valid zoom levels go from 0 to 18. See [Map options](https://developers.google.com/maps/documentation/javascript/tutorial#MapOptions) for details.

As for now, only fields using `FieldPanel` inside a `MultiFieldPanel` are supported. This is due to the lack of support of the `classname` attribute for other panel fields other than `MultiFieldPanel`.

In your `models.py`, your custom Page model would have something similar to:

```
address_panels = MultiFieldPanel([
    FieldPanel('address', classname="gmap"),
], heading="Street Address")
```

Notice the `FieldPanel` is embedded in a `MultiFieldPanel`, even if it only contains a single element. If you define your `FieldPanel` outside it won't work. The app supports more than one map (field) at the same time.

When editing the model from the admin interface the affected field shows up with a map, like the screenshot above.

The field gets updated according to the [Google Geocoding Service](https://developers.google.com/maps/documentation/geocoding/) each time:

* The map market gets dragged and dropped into a location (`dragend` JS event).
* Click happens somewhere in the map (`click` JS event).
* Return key is pressed after editing the field (`enterKey` JS event for return key only).

Feel free to edit the provided JS to add/edit the events you might need.

Once your address field is properly formatted and stored in the database you can use it in your front end Django templates. Example:

```
<a href="http://maps.google.com/?q={{ address }}">Open map</a>
```
