import tree_helpers

def postorder_traverse(tree_array):
    stack = [tree_array[0]]
    visited = []
    while len(stack) > 0:
        # is like a peek
        current = stack[0]
        current_item_index = tree_array.index(current)
        left = tree_helpers.left(tree_array, current_item_index)
        right = tree_helpers.right(tree_array, current_item_index)
        # travese left subtree
        if left is not None and left not in visited:
            stack.insert(0, left)
        # we've visited the left, so traverse the right subtree
        elif (left in visited or left is None) and (right is not None and right not in visited):
            print right
            stack.insert(0, right)
        # already visited both children or is a leaf itself
        elif (left in visited or left is None) and (right in visited or right is None):
            stack.pop(0)
            visited.append(current)           
    return visited
