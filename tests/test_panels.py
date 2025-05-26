import unittest

from django.conf import settings
from django.test import SimpleTestCase

from wagtailgmaps.panels import MapFieldPanel
from wagtailgmaps.widgets import MapInput


class EditHandlersTestCase(SimpleTestCase):
    def test_init_with_defaults(self):
        panel = MapFieldPanel("field-name")

        self.assertEqual(panel.default_centre, settings.WAGTAIL_ADDRESS_MAP_CENTER)
        self.assertEqual(panel.zoom, 8)
        self.assertEqual(panel.latlng, False)

    def test_init_with_values(self):
        panel = MapFieldPanel(
            "field-name",
            centre="somewhere",
            zoom=0,
            latlng=True,
        )

        self.assertEqual(panel.default_centre, "somewhere")
        self.assertEqual(panel.zoom, 0)
        self.assertEqual(panel.latlng, True)

    def test_clone(self):
        panel = MapFieldPanel(
            "field-name",
            centre="somewhere",
            zoom=0,
            latlng=True,
        )
        clone = panel.clone()

        self.assertEqual(panel.field_name, clone.field_name)
        self.assertEqual(panel.default_centre, clone.default_centre)
        self.assertEqual(panel.zoom, clone.zoom)
        self.assertEqual(panel.latlng, clone.latlng)

    @unittest.skip("TODO: Bind the panel to the model for the test to succeed.")
    def test_classes(self):
        panel = MapFieldPanel(
            "field-name",
            centre="somewhere",
            zoom=0,
            latlng=True,
        )
        classes = panel.classes()

        self.assertIn("wagtailgmap", classes)

    def test_widget_overrides(self):
        field_name = "field-name"
        panel = MapFieldPanel(
            field_name,
            centre="somewhere",
            zoom=0,
            latlng=True,
        )
        widget_overrides = panel.widget_overrides()

        self.assertIn(field_name, widget_overrides)
        self.assertIsInstance(widget_overrides[field_name], MapInput)
