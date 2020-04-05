# Time: O(n log n), space: O(1)
def areThereDuplicates(*args):

	i = 0
	j = 1
	args = list(args)
	args.sort()
	while(j < len(args)):
		if args[i]==args[j]:
			return True
		i += 1
		j += 1
	return False

print(areThereDuplicates('a', 'b', 'c', 'abc', 'e', 'bat', 'a'))

# Time and space: O(n)
# def areThereDuplicates(*args):
# 	# if len(args) in [0,1]:
# 	# 	return False
	
# 	freq = {}
# 	for arg in args:
# 		if arg not in freq:
# 			freq[arg] = 1
# 		else:
# 			return True
# 	return False