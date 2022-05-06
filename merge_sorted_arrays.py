# Example: arr1 = [0, 1, 3, 4], arr2 = [2, 3, 5]
# answer = [0, 1, 2, 3, 3, 4, 5]

# Time and space - O(n + m)
def merge_sorted_arrays(arr1, arr2):
  i = 0
  j = 0
  res = []
  
  while i < len(arr1) and j < len(arr2):
    first = arr1[i]
    second = arr2[j]
    if first <= second:
      res.append(first)
      i += 1
    else:
      res.append(second)
      j += 1

  if i == len(arr1):
    res = res + arr2[j:]
  else:
    res = res + arr1[i:]

  return res

print(merge_sorted_arrays([0, 1, 3, 4], [2, 3, 5]))