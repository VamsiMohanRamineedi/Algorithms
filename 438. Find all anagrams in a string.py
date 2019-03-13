# All anagrams in a string - Time: O(s), space: O(p)

class Solution:
    def findAnagrams(self, s: 'str', p: 'str') -> 'List[int]':
        result = []
        
        if len(s) == 0 or len(p) > len(s):
            return result
        
        p_chars = {}
        for char in p:
            if char not in p_chars:
                p_chars[char] = 1
            else:
                p_chars[char] += 1
        
        start = 0
        end = len(p)-1
        window = s[start:end+1]
        window_chars = {}
        for char in window:
                if char not in window_chars:
                    window_chars[char] = 1
                else:
                    window_chars[char] += 1
              
        while True:
            #print(start, end, window_chars)
            match = True
            for key in p_chars:
                if key not in window_chars or p_chars[key] != window_chars[key]:
                    match = False
                    break
            if match == True:
                result.append(start)
                #print(result)
            
            window_chars[s[start]] -= 1
            if window_chars[s[start]] == 0:
                del window_chars[s[start]]
            start += 1
            end += 1
            if end == len(s):
                break
            if s[end] not in window_chars:
                window_chars[s[end]] = 1
            else:
                window_chars[s[end]] += 1
        return result
             
        
        