# Binary Tree Inorder Traversal - Time and space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        visited, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return visited
            node = stack.pop()
            visited.append(node.val)
            root = node.right
'''
# Recursive
class Solution:
    def inorderTraversal(self, root):
        visited = []
        
        def helper(node):
            if not node:
                return []
            helper(node.left)
            visited.append(node.val)
            helper(node.right)
        helper(root)
        return visited

'''