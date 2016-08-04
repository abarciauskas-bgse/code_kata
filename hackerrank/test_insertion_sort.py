import pytest
from insertion_sort import *
import numpy as np

def test_function():
    for iteration in range(10):
        array_unsorted = list(np.random.choice(100,10))
        array_sorted = array_unsorted[:]
        array_sorted.sort()
        assert(insertion_sort(array_unsorted) == array_sorted)
