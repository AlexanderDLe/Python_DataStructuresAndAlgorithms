'''

  719. Find K-th Smallest Pair Distance

  [1,3,1] -> sort -> [1,1,3]
  
  L = 0, R = 3 - 1 = 2
  binary search across L -> R
  
  For each candidate, execute a 'feasible' method to check
  if distance is valid.
  
  k = 1
  
  ij
  [1,1,3]
  1-1 = 0
  
  i  j
  [1,1,3]
  1-1 = 0
  
  
  i    j
  [1,1,3]
  3-1 = 2
  
  

'''

class SolutionRef:
  def smallestDistancePair(self, nums, k):
    nums.sort()
    self.nums, self.k = nums, k
    
    L, R = 0, nums[-1] - nums[0]
    
    while L < R:
      M = L + (R - L)//2
      
      if self.feasible(M): R = M
      else               : L = M + 1
    
    return L
  
  def feasible(self, distance):
    count = i = j = 0
    nums, n = self.nums, len(self.nums)
    
    while i < n or j < n:
      while j < n and nums[j] - nums[i] <= distance:
        j += 1
      
      count += j - i - 1
      i += 1
    
    return count >= self.k
      
class Solution:
  def smallestDistancePair(self, nums, k):
    nums.sort()
    self.nums, self.k, self.n = nums, k, len(nums)
    L, R = 0, nums[-1] - nums[0] + 1
    
    while L < R:
      M = L + (R - L)//2
      if self.feasible(M): R = M
      else               : L = M + 1
      
    return L
  
  def feasible(self, distance):
    nums, k, n = self.nums, self.k, self.n
    i = j = count = 0
    
    while i < n or j < n:
      while j < n and nums[j] - nums[i] <= distance: j += 1
      
      count += j - i - 1
      i += 1
    
    return count >= k
        
      
  
def runSolution():
  solution = Solution()
  print(solution.smallestDistancePair(nums = [1,3,1], k = 1))
  print(solution.smallestDistancePair(nums = [1,1,1], k = 2))
  print(solution.smallestDistancePair(nums = [1,6,1], k = 3))
  pass
runSolution()
