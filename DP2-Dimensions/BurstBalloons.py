'''

  312. Burst Balloons        

'''

from itertools import product

class Solution:
  def maxCoins(self, nums):
    DP = {}
    
    def DFS(index):
      if index >= nums: return 0
      
      res = 0
      
      # Pop
      
      
      # Don't pop
      
      return res
    
      
    return DFS(0)
    
  
def runSolution():
  solution = Solution()
  print(solution.maxCoins(nums = [3,1,5,8]))
  print(solution.maxCoins(nums = [1,5]))
  pass
runSolution()