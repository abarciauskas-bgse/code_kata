class BinaryTree():
    # takes an array and creates a dictionary representing the tree
    # NOTE: this does not assert the tree is sorted (should it necessarily be?)
    def __init__(self, array):
        self.tree_dict = {}
        self.root = array[0]
        for index, value in enumerate(array):
            self.tree_dict[value] = {}
            lefti = 2*index+1
            righti = 2*index-1
            parenti = (index-1)/2
            self.tree_dict[value]['left_child'] = array[lefti] if (lefti < len(array)) else None
            self.tree_dict[value]['right_child'] = array[righti] if (righti < len(array)) else None
            self.tree_dict[value]['parenti'] = array[parenti] if (parenti >= 0) else None

    def traverse(self, method = 'inorder'): #, node_function):
        current = self.root
        if method == 'inorder':
            self.inorder_traverse(current)#, node_function)

    def inorder_traverse(self, current):
        if current is not None:
            self.inorder_traverse(self.tree_dict[current]['left_child'])
            print current
            self.inorder_traverse(self.tree_dict[current]['right_child'])


# Tests
import numpy as np
#rarray = np.sort(list(set(np.random.randint(20, size = 10))))
rarray = np.arange(0,10,1)
btree = BinaryTree(rarray)
print btree.tree_dict
print "Root: " + str(btree.root)
print ""
#btree.traverse()

