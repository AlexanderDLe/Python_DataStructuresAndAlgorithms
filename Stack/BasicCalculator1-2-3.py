'''

  Basic Calculator 1, 2, and 3
  

'''



class SolutionRef:
  def calculate(self, s):
    def calc(index):
      def update(sign, num):
        if sign == '+': stack.append(num)
        if sign == '-': stack.append(-num)
        if sign == '*': stack.append(stack.pop() * num)
        if sign == '/': stack.append(int(stack.pop() // num))
        
      num, stack, sign, = 0, [], '+'
      
      while index < len(s):
        char = s[index]
        
        if char.isdigit():
          num = num * 10 + int(char)
          
        elif char in '+-/*':
          update(sign, num)
          num, sign = 0, char
          
        elif char == '(':
          num, nextIndex = calc(index + 1)
          index = nextIndex
          
        elif char == ')':
          update(sign, num)
          return sum(stack), index
        
        index += 1
      update(sign, num)
      return sum(stack)
    
    return calc(0)
  
  

class Solution:
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
  

def runSolution():
  solution = Solution()
  # print(solution.calculate(s = "1 + 1"))
  # print(solution.calculate(s = " 2-1 + 2 "))
  print(solution.calculate(s = "- (3 + (4 + 5))"))
  print(solution.calculate(s = "(1+(4+5+2)-3)+(6+8)"))
  print(solution.calculate("2*(5+5*2)/3+(6/2+8)"))
  print(solution.calculate("5-3/2"))
  pass
runSolution()
