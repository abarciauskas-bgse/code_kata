# OLLD See tree ipynb
class BinaryTree():
    # takes an array and creates a dictionary representing the tree
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
    
    def breadth_first_search(self, search_value):
        # Using a queue, we first append the left and then right of the root node to the queue
        # then while the queue is non empty, we take the last item from the queue and explore and add it's children
        if search_value == self.root: return self.root
        queue = [self.root['right_child'], self.root['left_child']]
        while len(queue) > 0:
            node_data = queue.pop(-1)
            if node_data == search_value: return True # return index of?
            left_child = self.tree_dict[node_data]['left_child']
            right_child = self.tree_dict[node_data]['right_child']
            if left_child is not None:
                queue.insert(0, left_child)
            if right_child is not None:
                queue.insert(0, right_child)
        return False

    def height(self):
        height = 0
        last_index = len(self.array)-1
        parent = (last_index-1)/2
        while parent > 0:
            height += 1
            last_index = parent
            parent = (last_index-1)/2
        return height





# Tests
import numpy as np
#rarray = np.sort(list(set(np.random.randint(20, size = 10))))
rarray = np.arange(0,10,1)
btree = BinaryTree(rarray)
print btree.tree_dict
print "Root: " + str(btree.root)
print "Height: " + str(btree.height)
print ""
#btree.traverse()

