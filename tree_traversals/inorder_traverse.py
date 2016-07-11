import tree_helpers

def inorder_traverse(tree_array):
    stack = [tree_array[0]]
    visited = []
    while len(stack) > 0:
        last_item = stack[0]
        last_item_index = tree_array.index(last_item)
        left_child = tree_helpers.left(tree_array, last_item_index)
        if left_child is not None and left_child not in visited:
            stack.insert(0, left_child)
        else:
            visiting = stack.pop(0)
            visited.append(visiting)
            right_child = tree_helpers.right(tree_array, last_item_index)
            if right_child is not None: stack.insert(0, right_child)
    return visited

