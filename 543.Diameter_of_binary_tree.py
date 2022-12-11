# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n), space is O(log n) for average case and O(n) for worst case
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0
        
        def longest_path_from_node_to_leaf(node: Optional[TreeNode]) -> int:

            if node is None:
                return 0

            nonlocal diameter
    
            longest_left_path = longest_path_from_node_to_leaf(node.left)
            longest_right_path = longest_path_from_node_to_leaf(node.right)

            diameter = max(diameter, longest_left_path + longest_right_path)

            longest_path = max(longest_left_path, longest_right_path) + 1
            return longest_path
        
        longest_path_from_node_to_leaf(root)
        return diameter