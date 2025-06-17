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
        self.assertEqual(panel.latlngMode, False)

    def test_init_with_values(self):
        panel = MapFieldPanel(
            "field-name",
            centre="somewhere",
            zoom=0,
            latlngMode=True,
        )

        self.assertEqual(panel.default_centre, "somewhere")
        self.assertEqual(panel.zoom, 0)
        self.assertEqual(panel.latlngMode, True)

    def test_clone(self):
        panel = MapFieldPanel(
            "field-name",
            centre="somewhere",
            zoom=0,
            latlngMode=True,
        )
        clone = panel.clone()

        self.assertEqual(panel.field_name, clone.field_name)
        self.assertEqual(panel.default_centre, clone.default_centre)
        self.assertEqual(panel.zoom, clone.zoom)
        self.assertEqual(panel.latlngMode, clone.latlngMode)

    @unittest.skip("TODO: Bind the panel to the model for the test to succeed.")
    def test_classes(self):
        panel = MapFieldPanel(
            "field-name",
            centre="somewhere",
            zoom=0,
            latlngMode=True,
        )
        classes = panel.classes()

        self.assertIn("wagtailgmap", classes)
