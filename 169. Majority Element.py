# Majority Element
# Boyer-Moore Voting Algorithm - Time: O(n), space: O(1)

class Solution:
    
    def majorityElement(self, nums):
        count = 0
        selected = None
        
        for num in nums:
            if count == 0:
                selected = num
                count += 1
            elif selected == num:
                count += 1
            else:
                count -= 1
        return selected


'''
Majority element - Time: O(n), space: O(n)
class Solution:
    
    def majorityElement(self, nums: 'List[int]') -> 'int':
        # hash map
        length = len(nums)
        required = math.floor(length/2)
        hash_map = {}
        
        for number in nums:
            if number in hash_map:
                hash_map[number] += 1
            else:
                hash_map[number] = 1
            
            if hash_map[number] > required:
                return number
'''
        
        