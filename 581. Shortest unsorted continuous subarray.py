# Shortest Unsorted Continuous Subarray: Time - O(n), space - O(n)

class Solution:
    def findUnsortedSubarray(self, nums):
        left_boundary = len(nums)
        right_boundary = 0
        stack = []
        
        for index in range(len(nums)):
            while stack and nums[index] < nums[stack[len(stack)-1]]:
                left_boundary = min(left_boundary, stack.pop())
            stack.append(index)
            
        stack = []
        
        for index in range(len(nums)-1,-1,-1):
            while stack and nums[index] > nums[stack[len(stack)-1]]:
                right_boundary = max(right_boundary, stack.pop())
            stack.append(index)
        
        return right_boundary - left_boundary + 1 if right_boundary >= left_boundary else 0
