import unittest
from balance_factor import *

class TestBalanceFactor(unittest.TestCase):
    def test_balance_factor(self):
        tree_array = ['A', None, 'B', None, None, None, 'C']
        self.assertEqual(balance_factor(tree_array), {'A': -2, 'B': -1, 'C': 0})
