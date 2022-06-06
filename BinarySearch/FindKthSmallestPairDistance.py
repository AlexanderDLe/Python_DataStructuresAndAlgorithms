'''

  719. Find K-th Smallest Pair Distance

'''

class Solution:
  def smallestDistancePair(self, nums, k):
    nums.sort()
    self.nums, self.k = nums, k
    
    L, R = 0, nums[-1] - nums[0]
    
    while L < R:
      M = L + (R - L)//2
      
      if self.enough(M): R = M
      else             : L = M + 1
    
    return L
  
  def enough(self, distance):
    count = i = j = 0
    nums, n = self.nums, len(self.nums)
    
    while i < n or j < n:
      while j < n and nums[j] - nums[i] <= distance:
        j += 1
      
      count += j - i - 1
      i += 1
    
    return count >= self.k
      
  
def runSolution():
  solution = Solution()
  print(solution.smallestDistancePair(nums = [1,3,1], k = 1))
  print(solution.smallestDistancePair(nums = [1,1,1], k = 2))
  print(solution.smallestDistancePair(nums = [1,6,1], k = 3))
  pass
runSolution()
