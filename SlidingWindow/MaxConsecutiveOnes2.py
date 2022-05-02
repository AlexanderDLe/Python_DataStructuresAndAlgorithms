'''

  487. Max Consecutive Ones 2


'''

from collections import Counter

class Solution:
  def findMaxConsecutiveOnes(self, nums):
    L = maxLen = count = 0
    
    for R, Rchar in enumerate(nums):
      count += Rchar
      
      windowLen = R - L + 1
      flipsNeeded = windowLen - count
      
      if flipsNeeded <= 1:
        maxLen = max(maxLen, windowLen)
      
      if flipsNeeded > 1:
        count -= nums[L]
        L += 1
    
    return maxLen
    
    
    
  
def runSolution():
  solution = Solution()
  print(solution.findMaxConsecutiveOnes([1,0,1,1,0]))
  print(solution.findMaxConsecutiveOnes([1,0,1,1,0,1]))
  pass
runSolution()
