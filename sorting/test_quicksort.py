import unittest
from copy import deepcopy
import random
execfile('quicksort.py')

class QuicksortMethods(unittest.TestCase):

    def test_quicksort(self):
        array_length = 10
        test_array = [int(random.random()*100) for i in range(array_length)]
        test_array_copy = deepcopy(test_array)
        quicksort(test_array_copy, 0, len(test_array))
        test_array.sort()
        self.assertEqual(test_array_copy, test_array)
