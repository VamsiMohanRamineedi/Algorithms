# Product of Array except self  
# Time: O(n), space: O(1) - given in the question not to consider output array as extra space.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_product = 1
        right_product = 1
        output = []
        n = len(nums)
        
        for i in range(n):
            output.append(left_product)
            left_product *= nums[i]
        
        for i in range(n-1,-1,-1):
            output[i] *= right_product
            right_product *= nums[i]
            
        return output