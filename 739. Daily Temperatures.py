# Daily Temperatures: Time: O(n*m), space: O(n+m) - n: len of T; m: range of temperatures
class Solution(object):
    def dailyTemperatures(self, T):
        temperatures = {}
        result = [0] * len(T)
        for i in range(len(T))[::-1]:
            current = T[i]
            nearest = float('inf')
            for temp in temperatures:
                if temp > current:
                    nearest = min(nearest, temperatures[temp] - i)
            if nearest != float('inf'):
                result[i] = nearest
            temperatures[current] = i
        return result

'''
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not T:
            return T
        result = []
        temperature_dates = {} # key = temperature, value = list of days having that temperature
        for i in range(len(T)):
            if T[i] not in temperature_dates:
                temperature_dates[T[i]] = [i]
            else:
                temperature_dates[T[i]].append(i)
        
        result = []
        sorted_days = sorted(temperature_dates.keys())
        for i in range(len(T)):
            found = False
            for temp in sorted_days:
                if temp > T[i]:
                    if temperature_dates[temp][-1] < i:
                        continue
                    for day in temperature_dates[temp]:
                        if day > i:
                            if found:
                                if day-i < result[i]:
                                    result[i] = day-i
                            else:  
                                result.append(day - i)
                                found = True
                            break
                    if found and result[i] == 1:
                        break
            if not found:
                result.append(0)
        return result
'''