'''

  509. Fibonacci Number

'''

class Solution:
  def climbStairs(self, n):
    if n == 0: return 1
    
    DP = [1, 1]
    for _ in range(2, n + 1):
      DP = [DP[-1], DP[-1] + DP[-2]]
    
    return DP[-1]

class Solution:
  memo = {}
  
  def climbStairs(self, n):
    if n == 0 or n == 1: return 1
    if n-1 not in self.memo: self.memo[n-1] = self.climbStairs(n-1)
    if n-2 not in self.memo: self.memo[n-2] = self.climbStairs(n-2)
    return self.memo[n-1] + self.memo[n-2]
  
def runSolution():
  solution = Solution()
  print(solution.climbStairs(2))
  print(solution.climbStairs(3))
  print(solution.climbStairs(4))
  pass
runSolution()