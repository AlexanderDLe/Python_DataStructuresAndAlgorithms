'''

  1004. Max Consecutive Ones 3

'''

from collections import Counter

class Solution:
  def longestOnes(self, nums, k):
    L = count = maxLen = 0
    
    for R, Rnum in enumerate(nums):
      count += Rnum
      windowLen = R - L + 1
      flipsRequired = windowLen - count
      
      if flipsRequired <= k:
        maxLen = max(maxLen, windowLen)
        
      if flipsRequired > k:
        count -= nums[L]
        L += 1
    
    return maxLen
    
    
    
  
def runSolution():
  solution = Solution()
  print(solution.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
  print(solution.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))
  pass
runSolution()
