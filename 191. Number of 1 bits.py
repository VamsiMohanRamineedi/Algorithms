# Number of 1 bits - Time: O(log(n)), space: O(1)
# Point to note: Although we pass binary number to the function, we actually have n as decimal number inside the function.

class Solution(object):
    def hammingWeight(self, n):
        #print(n)
        count = 0
        while n:
            if n%2 == 1:
                count += 1
            n = n//2
        return count
        