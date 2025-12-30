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

    def test_set_mediator_type(self):
        self.mediator.set_mediator_type(Item("fadel"))
        self.assertIsInstance(self.mediator.item, Item)


class TestItemEmojiSmile(unittest.TestCase):

    item: Item = None

    def setUp(self):
        self.item = ItemEmojiSmile("fadel")
    def test_init(self):
        self.assertIsInstance(self.item, Item)

class TestEmojiItemHandler(self):
