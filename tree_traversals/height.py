from tree_helpers import *

heights = {}
def height(current, tree_array):
    if current is None:
        return [-1, -1]
    current_index = tree_array.index(current)
    left_child = left(tree_array, current_index)
    right_child = right(tree_array, current_index)
    if left_child or right_child:
        left_height = height(left_child, tree_array)[0]
        right_height = height(right_child, tree_array)[1]
        heights[current] = [left_height + 1, right_height + 1]
        print heights
        return heights[current]
    else:
        heights[current] = [0, 0]
        return [0, 0]

