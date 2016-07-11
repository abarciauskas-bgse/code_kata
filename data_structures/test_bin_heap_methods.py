import unittest
execfile('bin_heap.py')

class BinHeapTests(unittest.TestCase):
    def test_perc_up(self):
        bh = BinHeap()
        bh.heap_list = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27, 7]
        bh.perc_up(len(bh.heap_list)-1)
        self.assertEqual(bh.heap_list[1], 7)

    def test_insert(self):
        bh = BinHeap()
        bh.set_heap_list([5, 9, 11, 14, 18, 19, 21, 33, 17, 27])
        bh.insert(7)
        self.assertEqual(bh.heap_list[1], 7)

