'''

  772. Basic Calculator III
  
'''



class Solution:
  def calculate(self, s):
    stack = []
    num = 0
    op = '+'
    
    for char in s:
      if char.isnumeric():
        num = (num * 10) + int(char)
        continue
      
      
    
    pass
  
  

def runSolution():
  solution = Solution()
  print(solution.calculate(s = "1+1"))
  print(solution.calculate(s = "6-4/2"))
  print(solution.calculate(s = "2*(5+5*2)/3+(6/2+8)"))
  pass
runSolution()
