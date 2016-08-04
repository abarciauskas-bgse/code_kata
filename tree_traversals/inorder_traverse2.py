# inorder traverse, high level
# stack starts with the root
# while there is a left child, add it to the stack (using peek)
# else visit the last item
# append any right child to the stack

def inorder_traverse(root):
    stack = [root]
    visited = []
    while len(stack) > 0:
        last_item = stack.peek(0) # stack[0]
        if last_item.left is not None:
            stack.insert(0, last_item)
        else:
            visiting = stack.pop(0)
            visited.append(visiting)
            if visiting.right is not None:
                stack.insert(0, visiting.right)
    return visited

