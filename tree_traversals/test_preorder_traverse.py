import unittest
execfile('preorder_traverse.py')

class PreOrderTraverseMethods(unittest.TestCase):

    def test_inorder_traversal(self):
        tree_array = [7,1,9,0,3,8,10,None,None,2,5,None,None,None,None,None,None,None,None,None,None,4,6]
        self.assertEqual(preorder_traverse(tree_array), [7,1,0,3,2,5,4,6,9,8,10])
