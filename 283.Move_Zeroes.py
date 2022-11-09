# Time - O(n), space - O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0  # finds index of element 0
        j = 1  # finds index of non-zero element

        while j < len(nums):
            if nums[i] == 0:
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            else:
                i += 1
            j += 1
        return nums
