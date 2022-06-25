'''

  1567. Maximum Length of Subarray With Positive Product

    1  -2  -3  4
P   1   0
N   0   2
'''

class Solution:
  def getMaxLen(self, nums):
    maxLen = positives = negatives = 0
    
    for num in nums:
      if num == 0:
        positives = 0
        negatives = 0
        continue
      
      if num > 0:
        positives += 1
        negatives += 1 if negatives > 0 else 0
      
      if num < 0:
        temp = positives
        positives = 0 if negatives == 0 else negatives + 1
        negatives = temp + 1
        
      maxLen = max(maxLen, positives)
    
    return maxLen
  
def runSolution():
  solution = Solution()
  print(solution.getMaxLen(nums = [1,-2,-3,4]))
  print(solution.getMaxLen(nums = [0,1,-2,-3,-4]))
  print(solution.getMaxLen(nums = [-1,-2,-3,0,1]))
  print(solution.getMaxLen([-16,0,-5,2,2,-13,11,8]))
  pass
runSolution()