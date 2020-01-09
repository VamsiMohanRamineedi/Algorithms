# Time: O(J+S), Space: O(J)
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        all_jewels = {}
        result = 0
        for jewel in J:
            all_jewels[jewel] = 1
        for stone in S:
            if stone in all_jewels:
                result += 1
        return result
                
        
    
        