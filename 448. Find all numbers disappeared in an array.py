# Find all numbers disappeared in an array - Time: O(n), space: O(1)
class Solution:
    def findDisappearedNumbers(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return []
        
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
         
        return [i+1 for i in range(len(nums)) if nums[i] > 0]


'''
# Time - O(n), space - O(1) but program runs slow
class Solution:
    def findDisappearedNumbers(self, nums):
        
        if len(nums) == 0 or len(nums) == 1:
            return []
        
        swaps = 0
        i = 0
        while i < len(nums):
            if swaps == len(nums)-1:
                break
            val = nums[i]
            if val != i+1 and val != nums[val-1]:
                nums[val-1], nums[i] = val, nums[val-1]
                swaps += 1
                i -= 1
            i += 1
        
        return [i+1 for i in range(len(nums)) if nums[i] != i+1]
'''
        