# Time and space: O(n)
class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []
        count = 0

        for elem in s:
            if elem == '(':
                stack.append(elem)
            else:
                if stack:
                    stack.pop()
                else:
                    count += 1

        return len(stack) + count
