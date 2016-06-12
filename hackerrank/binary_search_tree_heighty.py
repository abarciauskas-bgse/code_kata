class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def getHeight(self, root):
        heights = {}
        heights[root] = 0
        max_height = 0
        stack = [root]
        while len(stack) > 0:
            current = stack.pop(0)
            left = current.left
            right = current.right
            if left is not None:
                heights[left] = heights[current] + 1
                stack.insert(0, left)
            if right is not None:
                heights[right] = heights[current] + 1
                stack.insert(0, right)
            if right is None and left is None:
                if heights[current] > max_height:
                    max_height = heights[current]
        return max_height

T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print height
