# Counting Bits - Time: O(n), space:O(n)
class Solution(object):
    def countBits(self, num):
        dp = [None] * (num+1)
        dp[0] = 0
        for i in range(1,num+1):
            if i%2 == 0:
                dp[i] = dp[i/2]
            else:
                dp[i] = 1 + dp[i//2]
        return dp
        
        
'''
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = []
        for i in range(num+1):
            count = 0
            while i:
                if i%2 == 1:
                    count += 1
                i = i//2
            result.append(count)
        return result
        
'''