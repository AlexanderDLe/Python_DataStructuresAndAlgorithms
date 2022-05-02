'''

  150. Evaluate Reverse Polish Notation

'''


from math import ceil, floor


class Solution:
  def evalRPN(self, token):
    stack = []
    
    for char in token:
      if char not in '+-*/':
        stack.append(int(char))
      else:
        top, pre = stack.pop(), stack.pop()
        if char == '+': stack.append(pre + top)
        if char == '-': stack.append(pre - top)
        if char == '*': stack.append(pre * top)
        if char == '/': 
          val = pre / top
          if val < 0: val = ceil(val)
          else      : val = floor(val)
          stack.append(val)
        
    return stack.pop()
  
def runSolution():
  solution = Solution()
  # print(solution.evalRPN(["2","1","+","3","*"]))
  # print(solution.evalRPN(["4","13","5","/","+"]))
  # print(solution.evalRPN(["10","6","9","3","+","-11"]))
  print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
  pass
runSolution()
