#Time - O(n), space - O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        req_sum = n * (n + 1) // 2
        given_sum = sum(nums)

        return req_sum - given_sum


'''
# Time and space - O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums_set = set(nums)
        for num in range(len(nums)+1):
            if num not in nums_set:
                return num
'''
