import unittest

from util import get_hue_from_hex


class UtilTestCase(unittest.TestCase):
    def test_yellow(self):
        hue = get_hue_from_hex('#ffff00')

        self.assertEqual(10922, hue)
