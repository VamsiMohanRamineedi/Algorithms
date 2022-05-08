# Time and space - O(n)
class Solution:
  def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
              
    res = []
    n = len(nums) - 1
    upper = float('-inf')
        
    for j, val in enumerate(nums):
        if val == key:
            lower = max(0, j - k, upper+1)
            upper = min(n, j + k)
            window = list(range(lower, upper+1))
            res += window
            if upper == n:
                break
    return res
                
        
        