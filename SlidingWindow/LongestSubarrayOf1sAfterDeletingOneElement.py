'''

  1493. Longest Subarray of 1's After Deleting One Element

'''

class Solution:
  def longestSubarray(self, nums):
    if nums.count(0) == 0: return len(nums) - 1
    L = maxLen = zeroes = 0
    
    for R, Rnum in enumerate(nums):
      if Rnum == 0: zeroes += 1
      
      if zeroes <= 1:
        maxLen = max(maxLen, R - L)
      
      if zeroes > 1:
        Lnum = nums[L]
        if Lnum == 0: zeroes -= 1
        L += 1
    
    return maxLen
  
def runSolution():
  solution = Solution()
  print(solution.longestSubarray([1,1,0,1]))
  print(solution.longestSubarray([0,1,1,1,0,1,1,0,1]))
  print(solution.longestSubarray([1,1,1]))
  pass
runSolution()
