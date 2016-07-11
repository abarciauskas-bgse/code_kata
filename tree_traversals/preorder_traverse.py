import tree_helpers

def preorder_traverse(tree_array):
    queue = [tree_array[0]]
    visited = []
    while len(queue) > 0:
        current = queue.pop()
        current_index = tree_array.index(current)
        visited.append(current)
        left = tree_helpers.left(tree_array, current_index)
        right = tree_helpers.right(tree_array, current_index)
        if right is not None: queue.append(right)
        if left is not None: queue.append(left)
    return visited
