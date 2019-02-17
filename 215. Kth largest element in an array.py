# Kth largest element in an array - Time: O(k + (n-k) log k), space: O(k)

class Solution:
    def findKthLargest(self, nums, k):
        # minheap
        array = nums[:k]
        heapq.heapify(array)
        for num in nums[k:]:
            if num > array[0]:
                heapq.heapreplace(array, num)
        return array[0]