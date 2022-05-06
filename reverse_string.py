# Time and space - O(n)
def reverse_string(my_str):

  if my_str is None or (not isinstance(my_str, str)):
    return "Check the input"
  
  reversed = ""
  for i in range(len(my_str)-1, -1, -1):
    reversed = reversed + my_str[i]

  return reversed

print(reverse_string("Hi, my name is Vamsi"))