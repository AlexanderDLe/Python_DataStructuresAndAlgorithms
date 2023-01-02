'''

  772. Basic Calculator III
  
'''



class Solution:
  def compute(self, stack, op, num):
    if op == '+': stack.append(num)
    if op == '-': stack.append(-num)
    if op == '*': stack.append(stack.pop() * num)
    if op == '/': stack.append(int(stack.pop() / num))
  
  def calc(self, s, index):
    op  = '+'
    num = 0
    stack = []
    
    while index < len(s):
      char = s[index]
      
      if char.isdigit():
        num = (num * 10) + int(char)
        
      elif char in '+-/*':
        self.compute(stack, op, num)
        op, num = char, 0
        
      elif char == '(':
        num, nextIndex = self.calc(s, index + 1)
        index = nextIndex
      
      elif char == ')':
        self.compute(stack, op, num)
        return sum(stack), index
      
      index += 1
    
    self.compute(stack, op, num)
    return sum(stack)
  
  def calculate(self, s):
    return self.calc(s, 0)
  

def runSolution():
  solution = Solution()
  print(solution.calculate(s = "1+1"))
  print(solution.calculate(s = "6-4/2"))
  print(solution.calculate(s = "2*(5+5*2)/3+(6/2+8)"))
  pass
runSolution()
