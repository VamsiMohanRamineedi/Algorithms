# Time - O(n) with n being the number of digits in the number (or) O(log10n) with n being the number.
# Space - O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0

        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half*10 + digit
            x //= 10
        
        return x == reversed_half or x == reversed_half//10


'''
# Time and space - O(n) with n being the number of digits in the number
class Solution:
    def isPalindrome(self, x: int) -> bool:

        x_str = str(x)
        
        if len(x_str) in [0, 1]:
            return True
        
        left = 0
        right = len(x_str) - 1

        while left < right:
            if x_str[left] != x_str[right]:
                return False
            left += 1
            right -= 1
        
        return True
'''