# Remove Outermost parentheses: Time and space: O(n)
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        output = ''
        remove = False
        primitive_stack = []
        
        for char in S:
            if not remove: # skips '(' in each primitive
                remove = True
            elif char == '(':
                output += char
                primitive_stack.append(char)
            elif primitive_stack:
                output += char
                primitive_stack.pop()
            elif not primitive_stack: # skips ')'
                remove = False
        return output      
                
'''
    def removeOuterParentheses(self, S):
        res, opened = [], 0
        for c in S:
            if c == '(' and opened > 0: res.append(c)
            if c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1
        return "".join(res)          
'''
            