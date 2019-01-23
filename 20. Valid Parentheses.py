# Valid Parentheses - Time: O(n), space: O(n)

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {'(':')', '[':']','{':'}'}
        stack = []
        for char in s:
            if char in ['(','[','{']:
                stack.append(char)
            elif char == (parentheses[stack[-1]] if stack else '#'):
                stack.pop()
            else: 
                return False
        return not stack
            
            
        
        
        