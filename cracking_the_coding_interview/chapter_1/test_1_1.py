# 1.1: Implement an algorithm to determine if a my_string has all unique characters What if you can not use additional data my_structures?
import pytest


def is_unique(my_str):
    my_str_len = len(my_str)
    if not my_str_len > 1: return True
    i = 0
    characeters_so_far = []
    while i < my_str_len:
        new_char = my_str[i]
        for j in characeters_so_far:
            if new_char == j:
                return False
        characeters_so_far.append(new_char)
        i+=1
        print ""
    return True

def test_answer():
    assert is_unique("abcde") == True
    assert is_unique("aacde") == False
    assert is_unique("a") == True
    assert is_unique("abb") == False
    assert is_unique("") == True
