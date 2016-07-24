import tree_helpers

def postorder_traverse(tree_array):
    stack = [tree_array[0]]
    visited = []
    while len(stack) > 0:
        # is like a peek
        current = stack[0]
        current_item_index = tree_array.index(current)
        left = tree_helpers.left(tree_array, current_item_index)
        if left is not None and left not in visited:
            stack.insert(0, left)
        else:
            right = tree_helpers.right(tree_array, current_item_index)
            if right is not None and right not in visited:
                stack.insert(0, right)
            else:
                visited.append(current)
                stack.pop(0)
    return visited
