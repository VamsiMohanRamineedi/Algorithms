# Maximum Subarray - Time: O(n), space - O(1)
class Solution:
    def maxSubArray(self, nums):
        
        if not nums:
            return None
        
        currentSum = 0
        largestSum = float('-inf')

        for num in nums:
            if currentSum + num >= 0:
                currentSum += num
                largestSum = max(largestSum, currentSum)
            else:
                currentSum = 0
        return max(nums) if largestSum == float('-inf') else largestSum        
