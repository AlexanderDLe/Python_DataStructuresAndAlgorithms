'''

  69. Sqrt(X)

'''

from math import floor


class Solution:
  def mySqrt(self, x):
    L, R = 0, x + 1
    
    while L < R:
      M = L + (R - L)//2
      
      if (M * M) <= x: L = M + 1
      else           : R = M
    
    return L - 1
  
  
def runSolution():
  solution = Solution()
  print(solution.mySqrt(4))
  print(solution.mySqrt(8))
  pass
runSolution()
