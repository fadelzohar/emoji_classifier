import unittest
from .temp import *

class TestTempItem(unittest.TestCase):
    item: Item = None
    def setUp(self):
        self.item = Item("fadel")

    def test_get_content(self):
        self.assertEqual(self.item.get_content(), "fadel")

    def test_set_type_id(self):
        self.assertIsInstance(self.item.set_type_id(2), Item)


class TestTextMediator(unittest.TestCase):

    mediator: TextMediator = None

    def setUp(self):
        self.mediator = TextMediator()

