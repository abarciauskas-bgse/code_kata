import pytest
import convert_to_binary as ctb

def test_function():
    assert ctb.convert_to_binary(15) == '0b1111' # i.e. same as bin(15) as implemented in python
    assert ctb.convert_to_binary(247) == '0b11110111'
