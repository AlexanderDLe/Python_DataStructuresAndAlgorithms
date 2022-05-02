'''

  1695. Maximum Erasure Value
  
'''

from collections import Counter


class Solution:
  def maximumUniqueSubarray(self, nums):
    freqMap = Counter()
    L, maxSum, currSum = 0, 0, 0
    
    for R, Rnum in enumerate(nums):
      freqMap[Rnum] += 1
      currSum += Rnum
      
      if freqMap[Rnum] < 2:
        maxSum = max(maxSum, currSum)
        
      while L < R and freqMap[Rnum] > 1:
        Lnum = nums[L]
        currSum -= Lnum
        L += 1
        freqMap[Lnum] -= 1
    
    return maxSum
    
    
    
  
def runSolution():
  solution = Solution()
  print(solution.maximumUniqueSubarray(nums = [4,2,4,5,6]))
  print(solution.maximumUniqueSubarray(nums = [5,2,1,2,5,2,1,2,5]))
  pass
runSolution()
