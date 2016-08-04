import unittest
execfile('rotations.py')

class RotationMethods(unittest.TestCase):
    def test_left_rotation(self):
        tree_array = ['A', None, 'B', None, None, None, 'C']
