def left(tree_array, index):
    left_index = 2*index + 1
    if len(tree_array) > left_index:
        return tree_array[left_index]
    else:
        return None

def right(tree_array, index):
    right_index = 2*index + 2
    if len(tree_array) > right_index:
        return tree_array[right_index]
    else:
        return None

def parent(tree_array, index):
    return tree_array[(index-1)/2]

def inorder_traverse(tree_array):
    stack = [tree_array[0]]
    visited = []
    while len(stack) > 0:
        last_item = stack[0]
        last_item_index = tree_array.index(last_item)
        left_child = left(tree_array, last_item_index)
        if left_child is not None and left_child not in visited:
            stack.insert(0, left_child)
        else:
            visiting = stack.pop(0)
            visited.append(visiting)
            right_child = right(tree_array, last_item_index)
            if right_child is not None: stack.insert(0, right_child)
    return visited

