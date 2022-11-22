# Time and space: O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        idx_to_remove = set()
        stack = []

        for idx, elem in enumerate(s):
            if elem == '(':
                stack.append(idx)
            elif elem == ')':
                if not stack:
                    idx_to_remove.add(idx)
                else:
                    stack.pop()
        
        idx_to_remove = idx_to_remove.union(set(stack))

        res = ''
        for idx, elem in enumerate(s):
            if idx not in idx_to_remove:
                res += elem

        return res