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
