# xor of two same numbers returns 0, and xor of 0 and a number returns the number.
# Time - O(n) and space - O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        res = 0
        for num in nums:
            res ^= num
        return res
