# Climbing Stairs: Time - O(n), space: O(1) - explanation written below
class Solution:
    def climbStairs(self, n):
        # we have the base cases: ways to reach level 1 = 1
        # ways to reach level 2 = 2
        if n == 1 or n == 2:
            return n
        
        # these variables represent the number of ways to reach to that level
        to_prev_to_current = 2 # initialized with current level assumed to be 3, so prev = level 2
        to_prev_to_prev = 1
        to_current = 0
        
        for current in range(3, n+1):
            to_current = to_prev_to_current + to_prev_to_prev
            to_prev_to_prev = to_prev_to_current
            to_prev_to_current = to_current
        return to_current

'''
# Climbing Stairs: Time - O(n), space: O(n)

# Let's say your goal is level 6. Try to think the possible ways of reaching level 6.
# One way is to jump 2 steps from level 4. Other way is to jump 1 step from level 5.
# So you can reach level 6 from either level 4 or level 5. For this to happen, you have
# to be in those levels first, and hence we need to calculate possible ways to reach 
# those levels.

# Ways to reach level 6 = ways to reach level 4 + ways to reach level 5

# You might think - 'I can also take 1 step + 1 step from level 4'. But when you take 
# the initial 1 step from level 4, you would reach level 5. And this case was already
# be counted in the 'ways to reach level 5'. So need not think about 1 step + 1 step 
# in this approach.

# Similar approach has to be followed for levels 4 and 5 till you reach base cases.

# Base cases: With the data given, we can easily say the ways to reach level 1 = 1;
# and the ways to reach level 2 = 2 (jumps of 1 step + 1 step, jump of 2 steps)

# The question reduces to fibonacci sequence with starting digits being 1 and 2.

class Solution:
    def climbStairs(self, n):
        cache = {} # save the data to avoid recalculations
        def helper(n):
            if n == 1 or n == 2:
                return n
            elif n in cache:
                return cache[n]
            else:
                cache[n] = helper(n - 1) + helper(n - 2)
                return cache[n]
        
        return helper(n)
'''
    
    
        
        