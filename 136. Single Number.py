#Single number - Time: O(n), space: O(1)
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result = result ^ num # XOR gives 0 if operated on same numbers/bits
        return result

'''
# Single Number - Time: O(n), space: O(n)
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                del hash_map[num]
        return [*hash_map][0] # [*hash_map] gives the hash map keys as a list
'''