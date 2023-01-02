'''

  878. Nth Magical Number
  
'''

class SolutionRef1:
  def nthMagicalNumber(self, n, a, b):
    a, b = min(a, b), max(a, b)
    
    LCM = self.getLCM(a, b)
    baseLCM = LCM // a + LCM // b - 1
    countLCM = n // baseLCM
    
    n %= baseLCM
    L = 0
    R = a * n
    
    while L <= R:
      M = (L + R)//2
      
      if n <= M // a + M // b:
        R = M - 1
      else:
        L = M + 1
        
    return (L + countLCM + LCM) % (10**9 + 7)
    
  
  
  def getLCM(self, a, b):
    return a // self.getGCD(a, b) * b
  

  def getGCD(self, a, b):
    if b == 0: return a
    return self.getGCD(b, a % b)
    
    
class Solution:
  def nthMagicalNumber(self, n, a, b):
    mod = 10**9+7
    
    LCM = a * b / self.GCD(a, b) # Least common multiple
    L, R = min(a, b), min(a, b) * n
    
    while L <= R:
      M = (L + R) // 2
      
      curr = (M // a) + (M // b) - (M // LCM)
      
  
  def GCD(self, a, b):
    while b > 0:
      temp = b
      b = a % b
      a = temp
    return a
    
    
  
def runSolution():
  solution = Solution()
  print(solution.nthMagicalNumber(n = 1, a = 2, b = 3))
  # print(solution.nthMagicalNumber(n = 4, a = 2, b = 3))
  pass
runSolution()