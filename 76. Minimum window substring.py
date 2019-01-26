# Minimum window substring - Time: O(s+t), space: O(s+t)

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ''
        
        start = 0
        end = 0
        chars_in_t = {}
        chars_in_window = {}
        min_length = float('inf')
        satisfied = 0
                
        for char in t:
            if char in chars_in_t:
                chars_in_t[char] += 1
            else:
                chars_in_t[char] = 1
                
        required = len(chars_in_t)
        
        while end < len(s):
            char = s[end]
            if char in chars_in_window:
                chars_in_window[char] += 1
            else:
                chars_in_window[char] = 1
            
            if (char in chars_in_t) and (chars_in_window[char] == chars_in_t[char]):
                satisfied += 1
                
                while satisfied == required:
                    if (end - start + 1) < min_length:
                        min_length = end - start + 1
                        result = s[start:end+1]
                        if min_length == len(t):
                            return result
                    left_char = s[start]
                    chars_in_window[left_char] -= 1
                    if left_char in chars_in_t and chars_in_window[left_char] < chars_in_t[left_char]:
                        satisfied -= 1
                    start += 1
            end += 1
        return '' if min_length == float('inf') else result               
        