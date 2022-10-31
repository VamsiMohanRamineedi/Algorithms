# Time and space - O(n)
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = Counter()

        for num in nums:
            if seen[num] == 1:
                return True
            seen[num] += 1
        return False
