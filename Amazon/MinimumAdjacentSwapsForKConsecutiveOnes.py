'''

  1703. Minimum Adjacent Swaps for K Consecutive Ones
  
'''


class SolutionRef:
  def minMoves(self, nums, k):
    p = [i for i, num in enumerate(nums) if num == 1]
    n = len(p)
    presum = [0] * (n + 1)
    for i in range(n):
      presum[i + 1] = presum[i] + p[i]
    print(p)
    print(presum)
    
    # Sliding window
    res = float('inf')
    
    if k % 2 == 1:
      # if odd
      radius = (k - 1)//2
      print(radius)
      for i in range(radius, n-radius):
        right = presum[i + radius + 1] - presum[i + 1]
        left  = presum [i] - presum[i - radius]
        res   = min(res, right - left)        
      return res - radius * (radius + 1)
    
    
    
    
    else:
      # even
      radius = (k-2)//2
      for i in range(radius, n-radius-1):
        right = presum[i+radius+2]-presum[i+1]
        left  = presum[i]-presum[i-radius]
        res   = min(res, right-left-p[i])        
      return res-radius*(radius+1)-(radius+1)
  
  
class Solution:
  def minMoves(self, nums, k):
    pass
  
def runSolution():
  solution = Solution()
  print(solution.minMoves(nums = [1,0,1,0,1,0,1,1,0,1,1,1], k = 5))
  # print(solution.minMoves(nums = [1,0,0,1,0,1], k = 2))
  # print(solution.minMoves(nums = [1,0,0,0,0,0,1,1], k = 3))
  pass
runSolution()
