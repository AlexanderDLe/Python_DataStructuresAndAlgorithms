'''

  509. Fibonacci Number

'''

class Solution:
  def fib(self, n):
    if n == 0: return 0
    
    DP = [0, 1]
    
    for _ in range(2, n + 1):
      DP = [DP[-1], DP[-1] + DP[-2]]
    
    return DP[-1]
  
def runSolution():
  solution = Solution()
  print(solution.fib(2))
  print(solution.fib(3))
  print(solution.fib(4))
  pass
runSolution()