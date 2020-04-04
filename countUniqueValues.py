# Time: O(n), space: O(n)

def returnUniqueValues(lst):
	res = []
	if len(lst) == 0:
		return res
	if len(lst) >= 1:
		res.append(lst[0])

	first = 0
	second = 1
	while(second < len(lst)):
		if lst[first] != lst[second]:
			res.append(lst[second])
			first = second
			second = first + 1
		else:
			second += 1
	return res


print(countUniqueValues([1,1,3,5,5,5,9]))