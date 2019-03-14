# Subtree of another tree
# m - no.of nodes in s; n - no.of nodes in t
# Time - O(mn), space - O(m+n)

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        if not self.isSameTree(s,t):
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        else:
            return True
    
    def isSameTree(self, t1, t2):
        
        if (not t1 and t2) or (not t2 and t1):
            return False
        
        if not t1 and not t2:
            return True
        
        if t1.val == t2.val:
            return self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)
        
        return False
        
        
        