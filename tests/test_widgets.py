from django.conf import settings
from django.test import SimpleTestCase, override_settings

from wagtailgmaps.widgets import MapInput


class MapInputTestCasse(SimpleTestCase):
    def _get_init_data(self, **kwargs):
        data = {
            'default_centre': 'Springload, Te Aro, Wellington, New Zealand',
            'zoom': 8,
            'latlng': False,
            'map_id': 'abcdef',
        }

        if kwargs:
            data.update(kwargs)

        return data

    def _get_widget(self):
        data = self._get_init_data()
        return MapInput(**data)

    def test_factory_is_valid(self):
        data = self._get_init_data()
        widget = MapInput(**data)

        self.assertEqual(widget.default_centre, data['default_centre'])
        self.assertEqual(widget.zoom, data['zoom'])
        self.assertEqual(widget.latlng, data['latlng'])
        self.assertEqual(widget.map_id, data['map_id'])

    @override_settings()
    def test_init_raises_for_missing_api_key(self):
        del settings.WAGTAIL_ADDRESS_MAP_KEY

        data = self._get_init_data()
        with self.assertRaises(Exception) as cm:
            MapInput(**data)

        self.assertEqual(str(cm.exception), 'Google Maps API key is missing from settings')

    def test_get_map_centre_for_none(self):
        data = self._get_init_data()
        widget = MapInput(**data)

        map_centre = widget.get_map_centre(None)
        self.assertEqual(map_centre, data['default_centre'])

    def test_get_map_centre_for_empty_value(self):
        data = self._get_init_data()
        widget = MapInput(**data)

        map_centre = widget.get_map_centre('')
        self.assertEqual(map_centre, data['default_centre'])

    def test_get_map_centre_with_value(self):
        data = self._get_init_data()
        widget = MapInput(**data)

        given_address = 'Torchbox, Charlbury, Chipping Norton, UK'
        map_centre = widget.get_map_centre(given_address)
        self.assertEqual(map_centre, given_address)

    def test_get_context(self):
        data = self._get_init_data()
        widget = MapInput(**data)

        expected_context = {
            'address': data['default_centre'],
            'zoom': data['zoom'],
            'map_id': data['map_id'],
            'latlng': data['latlng'],
            'gmaps_api_key': settings.WAGTAIL_ADDRESS_MAP_KEY,
        }
        context = widget.get_context('the-name', None, {})

        self.assertTrue(expected_context.items() <= context.items())

    def test_build_attrs_conserve_defaults(self):
        data = self._get_init_data()
        widget = MapInput(**data)

        base_attrs = {'id': 'abcdef'}
        attrs = widget.build_attrs(base_attrs)

        self.assertTrue(base_attrs.items() <= attrs.items())

    def test_build_attrs_sets_latlng(self):
        for latlng in (True, False):
            with self.subTest(latlng=latlng):
                data = self._get_init_data(latlng=latlng)
                widget = MapInput(**data)
                attrs = widget.build_attrs({})
                self.assertIn('data-latlng', attrs)
                self.assertEqual(attrs['data-latlng'], latlng)

    def test_render_js_init_method_name(self):
        data = self._get_init_data()
        widget = MapInput(**data)

        js_init = widget.render_js_init('the-id', 'the-name', 'the address')
        self.assertIn('window.initialize_map', js_init)

    def test_media_css(self):
        data = self._get_init_data()
        widget = MapInput(**data)

        css = widget.media._css
        self.assertEqual(len(css), 1)
        self.assertIn('screen', css)
        self.assertEqual(len(css['screen']), 1)
        self.assertEqual(css['screen'][0], 'wagtailgmaps/css/admin.css')

    def test_media_js(self):
        data = self._get_init_data()
        widget = MapInput(**data)

        js = widget.media._js
        self.assertEqual(len(js), 2)
        self.assertEqual(
            js[0], 'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.WAGTAIL_ADDRESS_MAP_KEY))
        self.assertEqual(js[1], 'wagtailgmaps/js/map-field-panel.js')

    @override_settings(WAGTAIL_ADDRESS_MAP_LANGUAGE='ru')
    def test_media_js_map_with_lang(self):
        data = self._get_init_data()
        widget = MapInput(**data)

        js = widget.media._js
        self.assertIn('&language=ru', js[0])
