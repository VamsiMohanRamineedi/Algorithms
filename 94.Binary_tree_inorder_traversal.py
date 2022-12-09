# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# inorder: left -> root -> right
# Iterative - Time and space - O(n)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = []
        res = []
        curr = root

        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                if stack:
                    curr = stack.pop()
                    res.append(curr.val)
                    curr = curr.right
                else:
                    break
        return res

'''
# Recursive - Time and space - O(n)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
'''