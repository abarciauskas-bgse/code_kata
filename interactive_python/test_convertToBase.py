import pytest

def convertToBase(number, base):
    if not type(base) == int:
        raise ValueError("Invalid data type for base: must be an int.")
    if not base <= 16 and base >= 2:
        raise ValueError("Invalid base: base must be an integer value between 2 and 16.")

    digits = "0123456789ABCDEF"
    rem_stack = []
    while number > 0:
        remainder = number % base
        rem_stack.insert(0, remainder)
        number = number // base

    new_string = ""
    while (len(rem_stack) > 0):
        new_string = new_string + digits[rem_stack.pop(0)]
    return new_string

print convertToBase(25, 8)
def test_function():
    assert convertToBase(233, 2) == "11101001"
    assert convertToBase(233, 8) == "351"
    assert convertToBase(233, 16) == "E9"
