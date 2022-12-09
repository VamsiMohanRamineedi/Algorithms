# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive solution. Time - O(n). Space is O(log n) average case, and O(n) worst case
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left: Optional[TreeNode],
                     right: Optional[TreeNode]) -> bool:

            #base cases
            if left is None and right is None:
                return True

            if (not left) or (not right) or (left.val != right.val):
                return False

            return isMirror(left.left, right.right) and isMirror(
                left.right, right.left)

        return isMirror(root.left, root.right)


'''
# Iterative solution - Time and space - O(n)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root.left is None and root.right is None:
            return True
        
        if not root.left or not root.right:
            return False

        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if (l.val != r.val) or (l.right and not r.left) or (not l.right and r.left) or \
                (l.left and not r.right) or (not l.left and r.right):
                return False
            if l.right and r.left:
                stack.append((l.right, r.left))
            if l.left and r.right:
                stack.append((l.left, r.right))
        return True
'''
