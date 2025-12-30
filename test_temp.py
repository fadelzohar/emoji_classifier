import unittest
from .temp import *

class TestTempItem(unittest.TestCase):
    item: Item = None
    def setUp(self):
        self.item = Item("fadel")


