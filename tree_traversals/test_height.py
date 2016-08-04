import unittest
from height import *

class TestHeight(unittest.TestCase):
    def test_height(self):
        tree_array = ['A', 'B', 'C', None, None, 'D', 'E', None, None, None, None, None, None, None, 'F']
        result = height('A', tree_array)
        self.assertEqual(result, {'A': [1,3], 'B': [0,0], 'C': [1,2], 'D': [0,0], 'E': [0,1], 'F': [0,0]})

