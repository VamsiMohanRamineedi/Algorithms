# Diameter of binary tree - Time: O(n) since we visit each node once. 
# space: O(n) since in worst case, our call stack can be of size n due to recursive calls

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.maxDiameter = 0
        
        def helper(node):
            depth_left = 0
            depth_right = 0
            
            if not node.left and not node.right:
                return 0
            
            depth_left = 1 + helper(node.left) if node.left else 0
            depth_right = 1 + helper(node.right) if node.right else 0           
            self.maxDiameter = max(self.maxDiameter, depth_left + depth_right)
            
            return max(depth_left, depth_right)
        
        helper(root)
        return self.maxDiameter
    
        