'''

  312. Burst Balloons        

'''

from itertools import product

class Solution:
  def maxCoins(self, nums):
     nums = [1] + nums + [1]
     print(nums)
     DP = {}
     
     def DFS(L, R):
       if (L, R) in DP: return DP[L, R]
       if L > R: return 0
       print(L, R)
       res = 0
       for i in range(L, R + 1):
         print(nums[L - 1], nums[i], nums[R + 1], nums[L - 1] * nums[i] * nums[R + 1])
         coins = nums[L - 1] * nums[i] * nums[R + 1]
         coins += DFS(L, i - 1)
         coins += DFS(i + 1, R)
         res = max(res, coins)
       
       DP[L, R] = res
       return res
     
     return DFS(1, len(nums) - 2)
    
  
def runSolution():
  solution = Solution()
  print(solution.maxCoins(nums = [3,1,5,8]))
  # print(solution.maxCoins(nums = [1,5]))
  pass
runSolution()