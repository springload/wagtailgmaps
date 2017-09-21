from __future__ import absolute_import, unicode_literals

import unittest

from wagtail.wagtailcore.hooks import get_hooks

from wagtailgmaps.wagtail_hooks import editor_css, editor_js


class TestWagtailHooks(unittest.TestCase):
    def test_editor_css(self):
        self.assertEqual(
            editor_css(),
            '<link rel="stylesheet" href="/static/wagtailgmaps/css/admin.css">'
        )

    def test_insert_editor_css_hook(self):
        hooks = get_hooks('insert_editor_css')
        self.assertIn(editor_css, hooks, 'Editor CSS should be inserted automatically.')

    # def test_editor_js(self):
    #     self.assertEqual(
    #         editor_js(), '<script src=""></script>')

    def test_insert_editor_js(self):
        hooks = get_hooks('insert_editor_js')
        self.assertIn(editor_js, hooks, 'Editor JS should be inserted automatically.')
