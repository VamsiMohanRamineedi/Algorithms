# Hamming Distance: Time - O(log(max(x,y))), space - O(1)
class Solution:
    def hammingDistance(self, x, y):
        if x==y:
            return 0
        count = 0
        while x or y: 
            x_bit = x % 2
            y_bit = y % 2
            
            if x_bit != y_bit:
                count += 1
            x = x//2
            y = y//2
        return count


'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x==y:
            return 0
        count = 0
        xor = x ^ y
        print(xor)
        print(bin(xor)[2:])
        for bit in bin(xor)[2:]:
            if bit == '1':
                count += 1
        return count
'''    