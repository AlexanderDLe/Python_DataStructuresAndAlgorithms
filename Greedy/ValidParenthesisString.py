'''

  678. Valid Parenthesis String
  
  (*)))
      ^
  stars = []
  stack = []
'''


class Solution2StacksMySolution:
  def checkValidString(self, s):
    stars = []
    stack = []
    
    for i, char in enumerate(s):
      if   char == '*': stars.append(i)
      elif char == '(': stack.append(i)
      else: 
        if not stars and not stack: 
          return False
        
        if not stack: 
          stars.pop()
          continue
        
        stack.pop()
    
    # If there are leftover opening parens and stars,
    # We can close the open if the index of the stars are after the open index
    while stack and stars:
      if stars[0] < stack[0]:
        stars.pop(0)
      else:
        stack.pop(0)
        stars.pop(0)
        
    return not stack
  
class Solution:
  def checkValidString(self, s):
    minLeft = 0
    maxLeft = 0
    
    for char in s:
      if char == '(':
        minLeft += 1
        maxLeft += 1
      elif char == ')':
        minLeft = max(0, minLeft - 1)
        maxLeft -= 1
      else:
        minLeft = max(0, minLeft - 1)
        maxLeft += 1

      if maxLeft < 0: return False
    
    return minLeft == 0
      
  
  
    

def runSolution():
  solution = Solution()
  print(solution.checkValidString(s = "()"))
  print(solution.checkValidString(s = "(*)"))
  print(solution.checkValidString(s = "(*))"))
  print(solution.checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))"))
  pass
runSolution()
