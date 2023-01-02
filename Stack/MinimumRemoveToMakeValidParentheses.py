'''

  1249. Minimum Remove to Make Valid Parentheses

  lee(t(c)o)de)
  
  stack = []
  
  Use stack to track open parens.
  If close parens encountered and stack has an open, then pop from stack.
  If close parens encountered and stack has no open, then invalidate close.
  If str ends with opens unmatched, then invalidate all opens in stack.
  
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

class Solution:
  
  '''

    Time Complexity:
    - O(n) passes through input string
    
    Space Complexity:
    - O(n) stack to hold indices
  
  '''
  
  def minRemoveToMakeValid(self, s):
    arr = list(s)
    stack = []
    
    for i, char in enumerate(arr):
      if char != '(' and char != ')': 
        continue
      
      elif char == '(':
        stack.append(i)
      
      elif char == ')':
        if stack: stack.pop()
        else         : arr[i] = ''
        
    while stack:
      arr[stack.pop()] = ''
    
    return ''.join(arr)
        
  
def runSolution():
  solution = Solution()
  print(solution.minRemoveToMakeValid("lee(t(c)o)de)"))
  print(solution.minRemoveToMakeValid("a)b(c)d"))
  print(solution.minRemoveToMakeValid("))(("))
  pass
runSolution()
