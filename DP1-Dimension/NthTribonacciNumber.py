'''

  1137. N-th Tribonacci Number

'''

class SolutionArray:
  def tribonacci(self, n):
    if n == 0: return 0
    
    DP = [0, 1, 1]
    
    for _ in range(3, n + 1):
      DP = [DP[-2], DP[-1], DP[-1] + DP[-2] + DP[-3]]
    
    return DP[-1]

class Solution:
  memo = {}
  
  def tribonacci(self, n):
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 1
    
    if (n-1) not in self.memo: self.memo[n-1] = self.tribonacci(n-1)
    if (n-2) not in self.memo: self.memo[n-2] = self.tribonacci(n-2)
    if (n-3) not in self.memo: self.memo[n-3] = self.tribonacci(n-3)
    
    return self.memo[n-1] + self.memo[n-2] + self.memo[n-3]
  
def runSolution():
  solution = Solution()
  print(solution.tribonacci(4))
  print(solution.tribonacci(25))
  pass
runSolution()