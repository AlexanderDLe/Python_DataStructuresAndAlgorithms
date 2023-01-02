'''

  921. Minimum Add to Make Parentheses Valid

'''



class SolutionRef:
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
  
  
class Solution:
  
  '''
  
    Time Complexity
    O(n) to iterate through string
    
    Space Complexity
    O(n) to hold items in stack
  
  '''
  
  def minAddToMakeValid(self, s):
    stack = []
    result = 0
    
    for char in s:
      if char == '(': 
        stack.append(char)
      elif char == ')' and stack:
        stack.pop()
      elif char == ')' and not stack:
        result += 1
        
    return result + len(stack)
  
def runSolution():
  solution = Solution()
  print(solution.minAddToMakeValid('())'))
  print(solution.minAddToMakeValid('((('))
  pass
runSolution()