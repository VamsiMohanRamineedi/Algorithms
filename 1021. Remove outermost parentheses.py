# Remove Outermost parentheses: Time and space: O(n)
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        open = 0
        result = ''
        
        for char in S:
            if open > 0 and char == '(':
                result += char
            elif open > 1 and char == ')':
                result += char
            open += 1 if char == '(' else -1
        return result

# A bit complex solution, but same time and space complexity
# class Solution:
#     def removeOuterParentheses(self, S: str) -> str:
#         output = ''
#         remove = False
#         primitive_stack = []
        
#         for char in S:
#             if not remove: # skips '(' in each primitive
#                 remove = True
#             elif char == '(':
#                 output += char
#                 primitive_stack.append(char)
#             elif primitive_stack:
#                 output += char
#                 primitive_stack.pop()
#             elif not primitive_stack: # skips ')'
#                 remove = False
#         return output      