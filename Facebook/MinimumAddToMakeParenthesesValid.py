'''

  921. Minimum Add to Make Parentheses Valid

'''

def minAddToMakeValid(s):
  stack = []
  count = 0

  for char in s:
    if char == '(': 
      stack.append(char)
    if char == ')':
      if len(stack) == 0: count += 1
      else              : stack.pop()
    
  return count + len(stack)




print(minAddToMakeValid('())'))
print(minAddToMakeValid('((('))