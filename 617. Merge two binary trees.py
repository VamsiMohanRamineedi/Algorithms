# Merge two binary trees - Time: O(m), space: O(log m) - m is the minimum number of nodes among two trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        
        # if not t1 and not t2: return None
        # ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        # ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        # ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        # return ans
        
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
        
        
                
        