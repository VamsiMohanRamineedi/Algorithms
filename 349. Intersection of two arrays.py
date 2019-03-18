# Intersection of two arrays: Time: O(m+n), space:O(m)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        hash_map_nums1 = {}
        for num in nums1:
            if num not in hash_map_nums1:
                hash_map_nums1[num] = 1
        for num in nums2:
            if num in hash_map_nums1:
                del hash_map_nums1[num]
                result.append(num)
        return result
                