import string

from django.test import SimpleTestCase

from wagtailgmaps import utils


class RandomStringTestCase(SimpleTestCase):
    def test_default_length(self):
        result = utils.random_string()
        self.assertEqual(len(result), 6)

    def test_default_charset(self):
        # Arguably it can't truly test that the function will never use characters form outside of the supplied charset
        # because randomness, but hopefuly the repetition (and length) should bring some confidence.
        for i in range(25):
            result = utils.random_string(length=100)

            for char in result:
                with self.subTest(char=char, i=i):
                    self.assertIn(
                        char, string.ascii_lowercase, msg='It should only use characters from the supplied set.')


    def test_custom_length(self):
        desired_length = 2
        result = utils.random_string(length=desired_length)
        self.assertEqual(len(result), desired_length)

    def test_custom_charset(self):
        supplied_charset = ['a']
        result = utils.random_string(chars=supplied_charset)

        for char in result:
            with self.subTest(char=char):
                self.assertIn(char, supplied_charset, msg='It should only use characters from the supplied set.')
