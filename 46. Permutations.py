# Permutations: Time - O(n!), space: O(n*n!)

class Solution(object):
    def permute(self, nums):
        res = []
        def dfs(available, formed):
            print(f'formed = {formed} ....... available = {available}')
            if len(formed) == len(nums):
                res.append(formed)
                print('Element added')
                return
            for i in range(len(available)):
                if available == nums:
                    print('--------')
                    print(f'permutations starting with {available[i]}')
                new_formed = formed + [available[i]] # form a new list
                new_available = available[:i] + available[i+1:] # remove the added number from availability
                dfs(new_available, new_formed)
            
        dfs(nums, [])
        return(res)

