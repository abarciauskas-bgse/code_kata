import unittest
execfile('inorder_traverse.py')

class InOrderTraverseMethods(unittest.TestCase):

    def test_helpers(self):
        tree_array = [8,3,10,1,6,None,14,None,None,4,7,None,None,13,None]
        self.assertEqual(parent(tree_array, 13), 14)
        self.assertEqual(right(tree_array, 2), 14)
        self.assertEqual(left(tree_array, 2), None)

    def test_inorder_traversal(self):
        tree_array = [8,3,10,1,6,None,14,None,None,4,7,None,None,13,None]
        self.assertEqual(inorder_traverse(tree_array), [1,3,4,6,7,8,10,13,14])

