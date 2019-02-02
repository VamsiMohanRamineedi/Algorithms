# Maximum Depth of binary tree - Time: O(n) since we visit each node once.
# space: O(n) in worst case scenario where there can be n recursive calls in the call stack.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        depth_left = self.maxDepth(root.left) if root.left else 0
        depth_right = self.maxDepth(root.right) if root.right else 0
        return max(depth_left, depth_right) + 1
            
        
        