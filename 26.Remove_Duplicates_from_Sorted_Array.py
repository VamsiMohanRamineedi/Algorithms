# Time - O(n), space - O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        insert_idx = 1
        i = 1

        while i < len(nums):
            if nums[i] != nums[i - 1]:
                nums[insert_idx] = nums[i]
                insert_idx += 1
            i += 1

        return insert_idx
