# Convert BST to Greater Tree: Time: O(n), space: O(log n) average case and O(n) worst case

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.total = 0
    
    def convertBST(self, root):
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root


'''
class Solution:
    def convertBST(self, root: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        self.sum = 0 # to maintain sum of the nodes on the right side
        
        def helper(node):
            
            # leaf node, sum will be sum till then plus leaf node value
            if not node.left and not node.right: 
                self.sum += node.val
                node.val = self.sum
                return self.sum
            
            # always traverse to the right most node in the tree, which is the largest value in BST
            if node.right:
                node.val += helper(node.right)
                self.sum = node.val
                    
            if not node.right:
                node.val += self.sum
            
            if node.left:
                self.sum = node.val
                return helper(node.left)
            return self.sum
        helper(root)
        return root
                
'''