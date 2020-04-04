# Time: O(n), space: O(1)

def returnUniqueValues(lst):
	if len(lst) in [0,1]:
		return lst

	first = 0
	second = first + 1
	while(second < len(lst)):
		if lst[first] != lst[second]:
			first += 1
			lst[first] = lst[second]
		second += 1
	return lst[:first+1]

# Time: O(n), space: O(n)
# def returnUniqueValues(lst):
# 	res = []
# 	if len(lst) == 0:
# 		return res
# 	if len(lst) >= 1:
# 		res.append(lst[0])

# 	first = 0
# 	second = 1
# 	while(second < len(lst)):
# 		if lst[first] != lst[second]:
# 			res.append(lst[second])
# 			first = second
# 			second = first + 1
# 		else:
# 			second += 1
# 	return res


print(f'unique values = {returnUniqueValues([1,1,1,3,3,5,5,5,9])}')