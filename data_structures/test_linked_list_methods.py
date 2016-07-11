import unittest
execfile('linked_list.py')

class MyTestCase(unittest.TestCase):
    def test_build(self):
        ll = LinkedList()
        data_array = [0, 9, 2, 7, 3, 0, 4, 5, 6, 2]
        ll.build(data_array)
        self.assertEqual(ll.get_head(), 2)
        self.assertEqual(ll.search(7), True)

    def test_remove_dups(self):
        ll = LinkedList()
        data_array = [0, 9, 2, 7, 3, 0, 4, 5, 6, 2]
        ll.build(data_array)
        self.assertEqual(ll.remove_dups(), 2)
        self.assertEqual(ll.size(), 8)
