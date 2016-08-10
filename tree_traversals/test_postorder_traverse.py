import unittest
execfile('postorder_traverse.py')

class PostOrderTraverseMethods(unittest.TestCase):

    def test_postorder_traversal(self):
        tree_array = [8,3,10,1,6,None,14,None,None,4,7,None,None,13,None]
        #self.assertEqual(postorder_traverse(tree_array), [1,4,7,6,3,13,14,10,8])
        tree_array = [7,1,9,0,3,8,10,None,None,2,5,None,None,None,None,None,None,None,None,None,None,4,6]
        #self.assertEqual(postorder_traverse(tree_array), [0,2,4,6,5,3,1,8,10,9,7])
        tree_array = [3,5,2,1,4,6]
        #self.assertEqual(postorder_traverse(tree_array), [1,4,5,6,2,3])
        tree_array = [3, 4, 12, 9, 11, 17, 23, 7, 8, 1, 0, -2, 19, 20, 6]
        self.assertEqual(postorder_traverse(tree_array), [7, 8, 9, 1, 0, 11, 4, -2, 19, 17, 20, 6, 23, 12   , 3])
