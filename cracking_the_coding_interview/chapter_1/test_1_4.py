# 1.4 Write a method to decide if two strings are anagrams or not
execfile('quicksort.py')

def is_anagram(str1, str2):
    str1 = list(str1.replace(' ','').lower())
    str2 = list(str2.replace(' ','').lower())
    len_str1 = len(str1)
    len_str2 = len(str2)   
    if not len_str1 == len_str2: return False
    if not len_str1 > 0: return False  
    quicksort(str1, 0, len_str1)
    quicksort(str2, 0, len_str2)    
    return str1 == str2

def test_answer():
    assert is_anagram("a","b") == False
    assert is_anagram("a", "a") == True # not sure about this one
    assert is_anagram("", "a") == False
    assert is_anagram("a", "") == False
    assert is_anagram("", "") == False
    assert is_anagram("cinema", "iceman") == True
    assert is_anagram("cinemas", "iceman") == False
    assert is_anagram("cinem", "iceman") == False
    assert is_anagram("Anna Madrigal", "A man and a girl") == True
