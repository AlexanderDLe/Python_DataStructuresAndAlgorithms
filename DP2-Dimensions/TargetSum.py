'''

  494. Target Sum              

'''

from itertools import product

class Solution:
  def findTargetSumWays(self, nums, target):
    n, DP = len(nums), {}
    
    def DFS(index, sum):
      if index in DP and sum in DP[index]: return DP[index][sum]
      if index == n:
        if sum == target: return 1
        return 0
      
      if index not in DP: DP[index] = {}
      add = DFS(index + 1, sum + nums[index])
      sub = DFS(index + 1, sum - nums[index])
      
      DP[index][sum] = add + sub
      return DP[index][sum]
    
    DFS(0, 0)
    return DP[0][0]
  
def runSolution():
  solution = Solution()
  print(solution.findTargetSumWays(nums = [1,1,1,1,1], target = 3))
  print(solution.findTargetSumWays(nums = [1], target = 1))
  pass
runSolution()