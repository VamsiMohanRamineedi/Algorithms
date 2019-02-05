# Symmetric Tree - Recursive Solution - Time: O(n), space: O(log n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        if left.val == right.val:
            outerPair = self.isMirror(left.left, right.right)
            innerPair = self.isMirror(left.right, right.left)
            return outerPair and innerPair
        return False



'''
# Iterative - Time: O(n), space: O(n)
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        
        # invert each child of nodes starting from root.left
        for node in self.traversebf(root.left):
            node.left, node.right = node.right, node.left        
        
        # check if root.left and root.right same trees
        return self.isSameTree(root.left, root.right)
        
    def traversebf(self, node):
        if not node:
            return []
        queue = [node]
        visited = []
        while queue:
            ele = queue.pop(0)
            if ele.left:
                queue.append(ele.left)
            if ele.right:
                queue.append(ele.right)
            visited.append(ele)
        return visited
    
    def isSameTree(self, p, q):
        if (not p and q) or (p and not q):
            return False
        
        if not p and not q:
            return True
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False
'''