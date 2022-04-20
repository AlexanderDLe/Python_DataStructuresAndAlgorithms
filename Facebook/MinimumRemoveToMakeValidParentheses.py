'''

  1249. Minimum Remove to Make Valid Parentheses

'''

def minRemoves(s):
  arr = list(s)
  stack = []
  
  for i, char in enumerate(arr):
    if char == ')':
      if len(stack) == 0: arr[i] = ''
      else              : stack.pop()

    if char == '(': 
      stack.append(i)

  while len(stack) > 0: arr[stack.pop()] = ''
  return ''.join(arr)

print(minRemoves("lee(t(c)o)de)"))
print(minRemoves("a)b(c)d"))
print(minRemoves("))(("))