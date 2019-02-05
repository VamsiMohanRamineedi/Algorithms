# Invert binart tree: Recursive - Time: O(n), space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        
        if not root:
            return None
         
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


'''
#Iterative - Time: O(n), space: O(n)
class Solution:
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        queue = [root]
        while queue:
            ele = queue.pop(0)
            ele.left, ele.right = ele.right, ele.left
            if ele.left:
                queue.append(ele.left) 
            if ele.right:
                queue.append(ele.right) 
        return root
'''