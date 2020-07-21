# Time and space: O(n)
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                comp_ind = seen[comp]
                return [comp_ind, i]
            else:
                seen[num] = i
            
        