import unittest
from .temp import *

class TestTempItem(unittest.TestCase):
    item: Item = None
    def setUp(self):
        self.item = Item("fadel")

    def test_get_content(self):
        self.assertEqual(self.item.get_content(), "fadel")

