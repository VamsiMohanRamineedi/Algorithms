# Time - O(m+n), space - O(min(m,n))
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # make sure nums1 is the smaller list
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # create hash map for the smaller list
        seen = Counter(nums1)
        insert_idx = 0
        for num in nums2:
            if seen[num] > 0:
                nums1[insert_idx] = num
                insert_idx += 1
                seen[num] -= 1
                if insert_idx == len(nums1):
                    break

        return nums1[:insert_idx]
