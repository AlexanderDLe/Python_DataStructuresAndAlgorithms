'''

  Basic Calculator 1, 2, and 3

'''



from typing import List



class SolutionRef:
  def calculate(self, s):
    def calc(index):
      def update(op, num):
        if op == '+': stack.append(num)
        if op == '-': stack.append(-num)
        if op == '*': stack.append(stack.pop() * num)       # BC 2 & 3
        if op == '/': stack.append(int(stack.pop() / num))  # BC 2 & 3
  
      num, op, stack = 0, '+', []
      
      while index < len(s):
        char = s[index]
        
        if char.isdigit():
          num = num * 10 + int(char)
          
        elif char in '+-*/':
          update(op, num)
          op, num = char, 0
          
        elif char == '(':                   # BC 1 & 3
          num, nextIndex = calc(index + 1)
          index = nextIndex
          
        elif char == ')':                   # BC 1 & 3
          update(op, num)
          return sum(stack), index
        
        index += 1
      update(op, num)
      return sum(stack)
    
    return calc(0)
  
class Solution:
  
  '''
  
    Time Complexity
    O(n) to iterate through all string characters
    
    Space Complexity
    O(n) to hold number values in stack
  
  '''
  
  def calculate(self, s):
    s = s.replace(' ', '')
    return self.calc(0, s)
    
  def calc(self, index, s):
    stack = []
    num = 0
    sign = '+'
    
    while index < len(s):
      char = s[index]
      
      if char.isdigit():
        num = (num * 10) + int(char)
      
      elif char in '+-/*':
        self.process(stack, sign, int(num))
        sign = char
        num = 0
        
      elif char == '(':
        num, nextIndex = self.calc(index + 1, s)
        index = nextIndex
        
      elif char == ')':
        self.process(stack, sign, num)
        return sum(stack), index
      
      index += 1
      
    self.process(stack, sign, num)
    return sum(stack)
        
  
  def process(self, stack: List[int], op, num):
    if op == '+': stack.append(num)
    if op == '-': stack.append(-num)
    if op == '*': stack.append(stack.pop() * num)
    if op == '/': stack.append(int(stack.pop() / num))

  
  
  

def runSolution():
  solution = Solution()
  # print(solution.calculate(s = "1 + 1"))
  # print(solution.calculate(s = " 2-1 + 2 "))
  # print(solution.calculate(s = "- (3 + (4 + 5))"))
  # print(solution.calculate(s = "(1+(4+5+2)-3)+(6+8)"))
  print(solution.calculate(s = "14-3/2"))
  # print(solution.calculate("2*(5+5*2)/3+(6/2+8)"))
  # print(solution.calculate("5-3/2"))
  pass
runSolution()
