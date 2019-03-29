# Validate BST - Time: O(n), space: O(logn) average case, O(n) worst case

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root, max_val=None, min_val=None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if max_val != None and root.val >= max_val:
            return False
        if min_val != None and root.val <= min_val:
            return False
        
        if (root.left and not self.isValidBST(root.left, root.val, min_val)) or (root.right and not self.isValidBST(root.right, max_val, root.val)):
            return False
        return True
        