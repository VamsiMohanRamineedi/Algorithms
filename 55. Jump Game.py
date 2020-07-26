class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        longest_reach_so_far = 0
        for curr_pos, max_jump in enumerate(nums):
            if longest_reach_so_far >= len(nums) - 1:
                return True
            elif curr_pos > longest_reach_so_far:
                return False
            longest_reach_so_far = max(longest_reach_so_far, curr_pos + max_jump)
            
                