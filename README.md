# wagtailgmaps [![PyPI](https://img.shields.io/pypi/v/wagtailgmaps.svg)](https://pypi.python.org/pypi/wagtailgmaps)

> Simple Google Maps address formatter and LatLng provider for [Wagtail](https://wagtail.io/) fields.

*Check out [Awesome Wagtail](https://github.com/springload/awesome-wagtail) for more awesome packages and resources from the Wagtail community.*

![Wagtailgmaps screenshot](./screenshot.png)

## Quickstart

``` $ pip install wagtailgmaps```

Add `wagtailgmaps` to your `settings.py` `INSTALLED_APPS` section.

Add a couple of necessary constants in your `settings.py` file:

```python
WAGTAIL_ADDRESS_MAP_CENTER = 'Wellington, New Zealand'
WAGTAIL_ADDRESS_MAP_ZOOM = 8
WAGTAIL_ADDRESS_MAP_KEY = 'xxx'
```

`WAGTAIL_ADDRESS_MAP_CENTER` must be a properly formatted address. Also, remember valid zoom levels go from 0 to 18. See [Map options](https://developers.google.com/maps/documentation/javascript/tutorial#MapOptions) for details.

> As of June 22 2016, Google maps requires an API key. See how to [Get a key](https://developers.google.com/maps/documentation/javascript/get-api-key). While you're there, you'll also need to enable the [Geocoding Service](https://developers.google.com/maps/documentation/javascript/geocoding).

wagtailgmaps expects a CharField (or any other field that renders as a text input) and comes with a MapFieldPanel. In your `models.py`, your custom Page model would have something similar to:

```python
address = models.CharField(max_length=255)
# ...

content_panels = [
    MapFieldPanel('address')
]
```

Notice that the string you pass to the `MapFieldPanel` is the name of the field, just like when using `FieldPanels`.

If instead of outputting a formatted address, you want to output a LatLng, you should add `latlng=True` to the panel:

```python
MapFieldPanel('address', latlng=True)
```

All the options available are:

 - `heading` - A custom heading in the admin, defaults to "Location"
 - `classname` - Add extra css classes to the field
 - `latlng` - Field returns a LatLng instead of an address
 - `centre` - A custom override for this field
 - `zoom` - A custom override for this field

When editing the model from the admin interface the affected field shows up with a map, like the screenshot above.

If using the address option, the field gets updated according to the [Google Geocoding Service](https://developers.google.com/maps/documentation/geocoding/) each time:

* The map marker gets dragged and dropped into a location (`dragend` JS event).
* Click happens somewhere in the map (`click` JS event).
* Return key is pressed after editing the field (`enterKey` JS event for return key only).

Feel free to edit the provided JS to add/edit the events you might need.

Once your address field is properly formatted and stored in the database you can use it in your front end Django templates. Example:

```html
<a href="http://maps.google.com/?q={{ address }}">Open map</a>
```

Or if you opted for the LatLng pair option:

```html
<a href="http://maps.google.com/?q={{ latlng }}">Open map</a>
```

## Development

### Releases

- Make a new branch for the release of the new version.
- Update the [CHANGELOG](https://github.com/springload/wagtailgmaps/CHANGELOG.md).
- Update the version number in `wagtailgmaps/__init__.py`, following semver.
- Make a PR and squash merge it.
- Back on master with the PR merged, use `make publish` (confirm, and enter your password).
- Finally, go to GitHub and create a release and a tag for the new version.
- Done!
