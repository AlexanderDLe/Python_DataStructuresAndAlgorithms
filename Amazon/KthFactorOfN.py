'''

  1492. The kth Factor of n

'''

import math


class SolutionBruteForce:
  def kthFactor(self, n, k):
    
    for i in range(1, n + 1):
      print(i)
      if n % i == 0: k -= 1
      if k == 0: return i
    
    return -1
  
class Solution:
  def kthFactor(self, n, k):
    factors = []
    
    for i in range(1, math.isqrt(n) + 1):
      if n % i == 0:
        factors.append(i)
        k -= 1
      if k == 0: return i
    
    print(factors)
    if factors[-1] ** 2 == n: factors.pop()
    if k > len(factors): return -1
    return n //factors[-k]
  
def runSolution():
  solution = Solution()
  print(solution.kthFactor(n = 12, k = 3))
  print(solution.kthFactor(n = 7, k = 2))
  print(solution.kthFactor(n = 4, k = 4))
  pass
runSolution()