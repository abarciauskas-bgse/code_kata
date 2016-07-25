import pytest
from fast_exponentiation import *
import random

def test_function():
    for itera in range(10):
        a = random.randint(0,10)
        n = random.randint(0,10)
        assert(fast_exponentiation(a, n) == a**n)
