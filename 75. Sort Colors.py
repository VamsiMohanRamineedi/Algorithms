# Go to https://leetcode.com/problems/sort-colors/discuss/751942/Easy-python-solution-for-beginners-with-explanation
# for my explanation

# Time: O(n), space: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums) - 1
        
        i = 0
        count = 0 # number of elements already sorted
        while count < len(nums):
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            count += 1
            
# Time and space: O(n)
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         seen = {}
#         for num in nums:
#             if num not in seen:
#                 seen[num] = 1
#             else:
#                 seen[num] += 1
                
#         idx = 0
#         for color in [0, 1, 2]:
#             if color in seen:
#                 while seen[color] != 0:
#                     nums[idx] = color
#                     idx += 1
#                     seen[color] -= 1
                
                
            