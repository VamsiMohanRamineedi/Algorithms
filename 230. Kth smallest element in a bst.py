# Kth smallest element in a BST: Time - O(n), space: O(log n) average case, O(n) worst case
class Solution(object):
    def kthSmallest(self, root, k):
        # Unlike inorder traversal method below which forms an array of ALL nodes, we cut off the search as soon as kth smallest is found.
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k = k-1
            if k==0:
                return root.val
            root = root.right
        
'''
class Solution(object):
    def kthSmallest(self, root, k):
        if not root:
            return root
        visited = []
        
        def inOrderTraverse(node):
            if node.left:
                inOrderTraverse(node.left)
            visited.append(node.val)
            if node.right:
                inOrderTraverse(node.right)
        
        inOrderTraverse(root)
        return visited[k-1]
        
'''