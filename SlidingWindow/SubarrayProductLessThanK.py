'''

  Subarray Product Less Than K
  
'''

class Solution:
  def numSubarrayProductLessThanK(self, nums, k):
    L, count, currProduct = 0, 0, nums[0]
    
    if currProduct < k: count += 1
    
    for R in range(1, len(nums)):
      Rnum = nums[R]
      currProduct *= Rnum
      
      if currProduct < k:
        count += (R - L + 1)
      
      while L < R and currProduct >= k:
        currProduct /= nums[L]
        L += 1
        
        if currProduct < k:
          count += (R - L + 1)
    
    return count
    
    
    
  
def runSolution():
  solution = Solution()
  print(solution.numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100))
  print(solution.numSubarrayProductLessThanK(nums = [1,2,3], k = 0))
  pass
runSolution()
