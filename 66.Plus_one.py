# Time - O(n) and space - O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits) - 1

        for i in range(n, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        return [1] + digits


'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)-1
        carry = 1

        for i in range(n, -1, -1):
            if digits[i] + carry != 10:
                digits[i] += carry
                if carry == 1:
                    carry = 0
            else:
                digits[i] = 0
                carry = 1
        
        return ([1] * carry) + digits
'''
