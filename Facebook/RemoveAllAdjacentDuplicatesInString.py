'''

  1047. Remove All Adjacent Duplicates in a String

'''

def removeDuplicates(s):
  stack = []

  for char in s:
    if stack and stack[-1] == char:
      stack.pop()
    else:
      stack.append(char)

  return ''.join(stack)




print(removeDuplicates('abbaca'))
print(removeDuplicates('azxxzy'))