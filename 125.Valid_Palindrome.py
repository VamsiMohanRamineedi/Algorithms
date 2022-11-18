# Time - O(n) and space - O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # allowed_chars = [str(num) for num in range(0, 10)]
        # for value in range(ord('a'), ord('a')+26):
        #     allowed_chars.append(chr(value))
        
        left = 0
        right = len(s)-1

        while left < right:
            left_char = s[left].lower()
            right_char = s[right].lower()
            if not left_char.isalnum():
                left += 1
            elif not right_char.isalnum():
                right -= 1
            else:
                if left_char != right_char:
                    return False
                else:
                    left += 1
                    right -= 1
        return True