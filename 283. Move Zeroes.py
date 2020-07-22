# 283. Move Zeroes - Time: O(n), space: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rep_idx = 0
        for i, num in enumerate(nums):
            if num != 0:
                if rep_idx != i:
                    nums[rep_idx], nums[i] = nums[i], nums[rep_idx]
                rep_idx += 1


# class Solution:
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         insertNonZeroElemIndex = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[insertNonZeroElemIndex], nums[i] = nums[i],nums[insertNonZeroElemIndex]
#                 insertNonZeroElemIndex += 1
#         return
                 
    

''' Time:O(n^2), space:O(1)

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        index = 0
        while index < len(nums):
            if count == len(nums):
                break
            if nums[index] == 0:
                del nums[index]
                nums.append(0)
                index -= 1
            count += 1
            index += 1
        return
'''
    
