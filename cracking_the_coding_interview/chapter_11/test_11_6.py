import pytest

alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
alphabet = str.split(alphabet) + [' ']
alphabet_dict = dict((el, i+1) for i,el in enumerate(alphabet))
dict_length = len(alphabet)

def string_hash_function(string):
    hash_value = 0
    nw = len(string)
    for idx in range(nw):
        letter = string[idx]
        hash_value += alphabet_dict[letter] * (pow(dict_length, nw-(idx+1)))
    return hash_value


def test_string_hash_function():
    assert(string_hash_function('cats') == 60337)

